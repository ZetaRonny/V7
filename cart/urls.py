from django.conf.urls import url
from django.urls import include, path

from .views import cart_home, cart_update


app_name = 'cart'

urlpatterns = [
	path('', cart_home, name='home'),
	path('update/', cart_update, name='update')
]