from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse('Hello, welcome to the index page.')