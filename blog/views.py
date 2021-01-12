from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render , redirect, get_object_or_404

# Create your views here.
def blog_detail_view(request, pk=None, *args, **kwargs):
	instance = get_object_or_404(Post, pk=pk)
	context = {
			'object': instance
	}
	return render(request,"blog/blog_detail.html", context)


class PostDetailSlugView(DetailView):
	queryset = Post.objects.all()
	template_name = "blog/blog_detail.html"

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		try: 
			instance = Post.objects.get(slug=slug)
		except Post.DoesNotExist:
			raise Http404('hehe not found')
		except Post.MultipleObjectsReturned:
			qs = Post.objects.filter(slug=slug)
			instance = qs.first()
		except:
			raise Http404('hoho not found')
		return instance

def blog_list_view(request):
	qs = Post.objects.all()
	context = {
			'object_list': qs
	}
	return render(request,"blog/blog_list.html",context)

