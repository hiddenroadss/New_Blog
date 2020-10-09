from django.urls import path
from .views import blogs_list_view

urlpatterns = [
	path('', blogs_list_view, name='blog-home'),
]
