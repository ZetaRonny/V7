from django.shortcuts import render, redirect
from .models import Cart
from V7_products.models import Product

# Create your views here.
def cart_home(request):
	cart_obj = Cart.objects.new_or_get(request)
	return render(request, 'carts/home.html', {"cart":cart_obj})

def cart_update(request):
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			return redirect("cart:home")
		cart_obj = Cart.objects.new_or_get(request) # new_obj
		cart_obj.products.add(product_obj)
	return redirect("cart:home")