from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Post
from django.shortcuts import render , redirect, get_object_or_404

# Create your views here.
def blog_detail_view(request, pk=None, *args, **kwargs):
	instance = get_object_or_404(Post, pk=pk)
	context = {
			'object': instance
	}
	return render(request,"blog/blog_detail.html", context)

def blog_list_view(request):
	qs = Post.objects.all()
	context = {
			'object_list': qs
	}
	return render(request,"blog/blog_list.html",context)

