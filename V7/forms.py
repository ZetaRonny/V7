# forms.py

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.CharField()
	password = forms.CharField()
	confirm_password = forms.CharField()

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=eamil)
		if qs.exist():
			return forms.ValidationError('email exists in our system')
		return email

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			return forms.ValidationError("username exists select new one")
		return username

	def clean(self):
		data =  self.cleaned_data
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError('passwords must match')
		return data



