from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from privacy.models import Policy
import form

def index(request):
	if request.method == 'POST':
		p_id = request.POST.get('id', False)
		print p_id
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
			print name, view, displen, delete, datause, tracking, gps
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
	context = p_id
	return HttpResponse("Here's the id: %s" % p_id)