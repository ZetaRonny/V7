from django.http import JsonResponse
from .models import Product, Manufacturer


def product_list(request):
	products = Product.objects.all()
	data = {"products": list(products.values())}
	response = JsonResponse(data)
	return response

def product_detail(request, pk):
	try:
		product = Product.objects.get(pk=pk)
		data = {"product": {
					"name": product.name,
					"description":product.description,
					}}
		response = JsonResponse(data)
	except Product.DoesNotExist:
		response = JsonResponse({
				"err":{
						"code": 404,
						"message":"product not found!"
				}},
			status=404)
	return response