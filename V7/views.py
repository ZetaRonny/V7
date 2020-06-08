from django.http import HttpResponse
from django.shortcuts import render


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
