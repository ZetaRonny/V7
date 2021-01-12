from django.urls import path
from .views import blog_list_view , PostDetailSlugView


app_name = "blog"

urlpatterns = [
	path("", blog_list_view, name="list"),
	path("<str:slug>", PostDetailSlugView.as_view(), name="detail"),
]
