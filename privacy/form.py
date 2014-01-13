from django.forms import ModelForm
from privacy.models import Policy

class PolicyForm(ModelForm):
	class Meta:
		model = Policy