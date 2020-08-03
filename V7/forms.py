# forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

class ContactForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	message = forms.CharField(max_length=1024, widget=forms.TextInput(attrs={'class' : 'form-control'}))

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
	confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=eamil)
		if qs.exist(widget=forms.TextInput(attrs={'class' : 'form-control'})):
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



