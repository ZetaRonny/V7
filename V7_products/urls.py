from django.urls import path
from .views import product_list_view, ProductDetailSlugView

app_name = 'products' 

urlpatterns = [
	path("", product_list_view, name="list"),
	path("<str:slug>/", ProductDetailSlugView.as_view(), name='detail')
]