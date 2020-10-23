from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = 'all_blogs'
    ordering = ['-date_created']
    paginate_by = '5'


class UserBlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_by_user_list.html'
    context_object_name = 'all_blogs'
    paginate_by = '5'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.filter(author=user).order_by('-date_created')


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']

    def test_func(self):
        blog = self.get_object()
        if blog.author == self.request.user:
            blog.author = self.request.user
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if blog.author == self.request.user:
            blog.author = self.request.user
            return True
        return False
