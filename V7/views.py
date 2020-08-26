from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import LoginForm , RegisterForm , ContactForm

def index(request):
	context = {"title":"V7",} 
	return render(request,'index.html', context)

def about(request):
	context = {"title":"About",}
	return render(request, 'about.html', context)

def thankyou(request):
	context = {"title":"thank you"}
	return render(request, 'contact/thankyou.html', context)

def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			message = form.cleaned_data.get('message')
			email = form.cleaned_data.get('email')
			try:
				send_mail(
				'message from ' + username, # subject
				 message,
				 email,
				 ['ContactVariantSeven@gmail.com'],
				)
			except BadHeaderError:
				return HttpResponse('invalid header found.')
			return redirect('/thankyou')
	context = {
		"title":"Contact",
		"form": form
	} 
	return render(request, 'contact/contact.html', context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {"form": form}
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request,user)
			context['form'] = LoginForm()
			return redirect("index")
		else:
			print('err')
	return render(request,'auth/login_template.html', context)


def register_page(request):
	user = get_user_model()
	form = RegisterForm(request.POST or None)
	context = {"form": form}
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		email = form.cleaned_data.get('email')
		confirm_password = form.cleaned_data.get('confirm_password')
		user.objects.create_user(username, email, password)  
		# authenticate email 
	return render(request,'auth/register_template.html', context)