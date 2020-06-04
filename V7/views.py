from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def index(request):
	context = {"title":"V7",} 
	return render(request,'base_template.html', context)

def about(request):
	context = {"title":"About",}
	return render(request, 'base_template.html', context)

def contact(request):
	form = ContactForm()
	context = {
	"title":"Contact",
	"form": form,
	} 
	return render(request, 'base_template.html', context)
