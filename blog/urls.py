from .views import blog_list_view , blog_detail_view

urlpatterns = [
	path("blog/", blog_list_view, name="blog-list-view"),
	path("blog/<pk>", blog_detail_view, name="blog-detail-view"),
]
