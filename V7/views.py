from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import LoginForm , RegisterForm

def index(request):
	context = {"title":"V7",} 
	return render(request,'base_template.html', context)

def about(request):
	context = {"title":"About",}
	return render(request, 'base_template.html', context)

def contact(request):
	context = {
	"title":"Contact",
	} 
	return render(request, 'base_template.html', context)


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
			# return redirect("/admin")
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