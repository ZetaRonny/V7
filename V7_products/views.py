from django.http import JsonResponse , Http404
from django.views.generic import ListView , DetailView
from .models import Product, Manufacturer
from django.shortcuts import render , redirect, get_object_or_404

def product_list_view(request):
	qs = Product.objects.all()
	context = {
			'object_list': qs
	}
	return render(request,"products/product_list.html",context)

def product_detail_view(request, pk=None, *args, **kwargs):
	instance = get_object_or_404(Product, pk=pk)
	if instance is None:
		raise Http404("product is not found")


	context = {
			'object': instance
	}
	return render(request,"products/product_detail.html", context)