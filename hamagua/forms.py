from django import forms
from django.forms import ModelForm
from models import Target

class TargetForm(ModelForm):
	class Meta:
		model = Target
		fields=('name','time_allownace','comment')

