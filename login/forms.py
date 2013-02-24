
from django.forms import ModelForm
from django.contrib.auth.models import User  


class UserRegisterForm(ModelForm):
	class Meta:
		model = User
		fields=('username','password','email')

