from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from privacy.models import Policy, PostedData, Authority
import form

global pk
global policy

def index(request):
	if request.method == 'POST':
		p_id = request.POST.get('id', False)
		if p_id:
			name = request.POST.get('name', "")
			user = Policy.objects.get(pk=int(p_id))
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
	if request.method == 'POST':
		content = request.POST.get('status', False)
		if content:
			p = PostedData(p_id=int(p_id), status=content)
			p.save()
			return HttpResponseRedirect('')
		else:
			return render(request, 'policy.html', {'msg': 'You didn\'t enter a status. Please try again.', 'id': p_id, 'name': user.name})

	statuses = PostedData.objects.filter(p_id=int(p_id))
	context = {'statuses': statuses, 'id': p_id, 'name': user.name}		
	return render(request, 'policy.html', context)

def authority(request):
	if (request.is_ajax()):
		name = request.GET.get('name', False)
		policy = request.GET.get('policy', False)
		attr_list = request.GET.getlist('list', False)
		print name, policy, attr_list
		if name and policy and attr_list:
			pk = 1234567890
			mk = 987654321
			a = Authority(app_name=name, pk=pk, mk=mk, attr_list=attr_list)
			a.save()
			print pk, mk, name, policy
			msg = 'Success!'
			return render(request, 'authority.html', {'msg': msg})
		else:
			msg = 'Failed.'
			return render(request, 'authority.html', {'msg': msg})
	else:
		return render(request, 'authority.html');









