from django.urls import path

from .views import BlogListView, BlogDetailView, BlogUpdateView, BlogCreateView, BlogDeleteView, UserBlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-home'),
    path('articles_by/<str:username>/', UserBlogListView.as_view(), name='blog-by-user'),
    path('article/create/', BlogCreateView.as_view(), name='blog-create'),
    path('article/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('article/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('article/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
]
