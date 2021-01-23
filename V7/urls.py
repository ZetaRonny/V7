"""V7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import blog_list_view , blog_detail_view
from search.views import SearchView
from cart.views import cart_home
from .views import login_page, register_page, index , contact, thankyou , faq


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/", include("V7_products.urls")),
    path('products/', include('V7_products.urls'), name='Products'),
    path("login/", login_page, name='Login'),
    path("register/", register_page, name='Register'),
    path('thankyou/', thankyou, name='Thankyou'),
    path('faq/', faq, name='FAQ'),
    path('', index, name='Index'),
    path('blog/', include('blog.urls'), name='Blogs'),
    path('contact/', contact, name='Contact'),
    path('cart/', include('cart.urls'), name='Cart'),
    path('search/', SearchView.as_view(), name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
