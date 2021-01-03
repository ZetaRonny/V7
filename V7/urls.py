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
from V7_products.views import product_list_view, product_detail_view
from blog.views import blog_list_view , blog_detail_view
from .views import login_page, register_page, index , contact, thankyou , faq


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/", include("V7_products.urls")),
    path('products/', product_list_view , name="Products"),
    path('products/<pk>/', product_detail_view),
    path("login/", login_page, name='Login'),
    path("register/", register_page, name='Register'),
    path('thankyou/', thankyou, name='Thankyou'),
    path('faq/', faq, name='FAQ'),
    path('', index, name='Index'),
    path('blog/', blog_list_view, name='Blogs'),
    path('blog/<pk>/', blog_detail_view, name='blog-detail-view'),
    path('contact/', contact, name='Contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
