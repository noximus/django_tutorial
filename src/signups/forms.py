from django import forms

#create your views here.
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp