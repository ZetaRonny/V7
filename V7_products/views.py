from django.http import JsonResponse , Http404
from django.views.generic import ListView , DetailView
from django.shortcuts import render , redirect, get_object_or_404

from .models import Product, Manufacturer
from cart.models import Cart

def product_list_view(request):
	qs = Product.objects.all()
	context = {
			'object_list': qs
	}
	return render(request,"products/product_list.html",context)

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/product_detail.html"

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		try: 
			instance = Product.objects.get(slug=slug)
		except Product.DoesNotExist:
			raise Http404('hehe not found')
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug)
			instance = qs.first()
		except:
			raise Http404('hoho not found')
		return instance

def product_detail_view(request, pk=None, *args, **kwargs):
	instance = get_object_or_404(Product, pk=pk)
	if instance is None:
		raise Http404("product is not found")


	context = {
			'object': instance
	}
	return render(request,"products/product_detail.html", context)