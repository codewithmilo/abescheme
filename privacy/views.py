from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from privacy.models import Policy, PostedData, Authority
from Charm.charm.adapters import abenc_adapt_hybrid as charm
from charm.core.engine.util import objectToBytes,bytesToObject
from django.core.exceptions import ObjectDoesNotExist
import form
import json

global groupObj
global cpabe
global hyb_abe
groupObj = charm.PairingGroup('SS512')
cpabe = charm.CPabe_BSW07(groupObj)
hyb_abe = charm.HybridABEnc(cpabe, groupObj)

def index(request):
	if request.method == 'POST':
		p_id = request.POST.get('id', False)
		if p_id:
			name = request.POST.get('name', "")
			try:
				user = Five.objects.get(name=username)
			except ObjectDoesNotExist:
				user = False
			if user.name == name:
				return HttpResponseRedirect(p_id)
			else:
				return render(request, 'index.html', {'msg': 'A user with that ID was not found. Please try again.', 'form': form.PolicyForm()})

		else:
			name = request.POST.get('id_name', False)
			view = request.POST.get('viewers', False)
			displen = request.POST.get('viewlen', False)
			delete = request.POST.get('deleted', False)
			datause = request.POST.getlist('datause', False)
			tracking = request.POST.get('track', False)
			gps = request.POST.get('gps', False)
			if name and view and displen and delete and datause and tracking and gps:
				p = Policy(name=name, viewers=view, display_length=displen, deleted_length=delete, data_use=datause, tracking=tracking, gps_loc=gps)
				p.save()
				new_user = Policy.objects.get(name=name)
				p_id = new_user.id
				return HttpResponseRedirect(str(p_id))
			else:
				return render(request, 'index.html', {'msg': 'There was a mistake in your form entries. Please try again.', 'form': form.PolicyForm()})

	return render(request, 'index.html', {'form': form.PolicyForm()})

def policy(request, p_id):
	user = Policy.objects.get(pk=int(p_id))
	appname = "privateBook"
	statuses_decrypted = []
	if request.method == 'POST':
		content = request.POST.get('status', False)
		if content:
			try:
				auth = Authority.objects.get(app_name=appname)
			except ObjectDoesNotExist:
				auth = False
			if auth:
				private = bytesToObject(auth.p_key, groupObj)
				decoder = bytesToObject(auth.d_key, groupObj)
				print content, auth.policy
				encrypt = hyb_abe.encrypt(private, str(content), str(auth.policy))
				print encrypt
				encrypt_b = objectToBytes(encrypt, groupObj)
				p = PostedData(p_id=int(p_id), status=encrypt_b)
				p.save()
			else:
				return render(request, 'policy.html', {'msg': 'The authority has not created any keys for you to encrypt your data!', 'id': p_id, 'name': user.name})
			return HttpResponseRedirect('')
		else:
			return render(request, 'policy.html', {'msg': 'You didn\'t enter a status. Please try again.', 'id': p_id, 'name': user.name})

	try:
		auth = Authority.objects.get(app_name=appname)
	except ObjectDoesNotExist:
		auth = False
	if auth:
		statuses = PostedData.objects.filter(p_id=int(p_id))
		for s in statuses:
			print s.status
			status_cipher = bytesToObject(s.status, groupObj)
			print status_cipher
			private = bytesToObject(auth.p_key, groupObj)
			decoder = bytesToObject(auth.d_key, groupObj)
			# make a pair (status, time) to add to the list, then change policy.html
			statuses_decrypted.append(hyb_abe.decrypt(private, decoder, status_cipher))
			print statuses_decrypted
	if statuses_decrypted:
		context = {'statuses': statuses_decrypted, 'id': p_id, 'name': user.name}
	else:
		context = {'msg': 'Your statuses could not be displayed due to lack of Authority.', 'id': p_id, 'name': user.name}		
	return render(request, 'policy.html', context)

def authority(request):
	if (request.is_ajax()):
		name = request.GET.get('name', False)
		policy = request.GET.get('policy', False)
		attr_list = request.GET.getlist('list', False)
		attr_list = [x.encode('UTF8') for x in attr_list]
		print name, policy, attr_list
		if name and policy and attr_list:
			(private, master) = hyb_abe.setup()
			print attr_list
			decoder = hyb_abe.keygen(private, master, attr_list)
			decoder_b = objectToBytes(decoder, groupObj)
			private_b = objectToBytes(private, groupObj)
			try:
				a = Authority.objects.get(app_name=name)
			except ObjectDoesNotExist:
				a = Authority(app_name=name, attr_list=attr_list, policy=policy, p_key=private_b, d_key=decoder_b)
				a.save()
			json_res = {'msg': 'Success!'}
		else:
			json_res = {'msg': 'Failure.'}

		return HttpResponse(json.dumps(json_res), content_type='application/json')

	return render(request, 'authority.html');

