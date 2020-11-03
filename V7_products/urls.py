from django.urls import path
from .views import productListView

urlpatterns = [
	path("products/", productListView, name="product-list-view"),
]