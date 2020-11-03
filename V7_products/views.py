from django.http import JsonResponse
from django.views.generic import ListView
from .models import Product, Manufacturer

class productListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/product_list.html"

	# def get_context_data(self, *args,  **kwargs):
	# 	context = super(productListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


def product_list_view(request):
	qs = Product.objects.all()
	context = {
			'object_list': qs
	}
	return render(request,"products/product_list.html",context)