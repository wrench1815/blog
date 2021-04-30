from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


class BlogPostsListView(ListView):
    model = Post
    template_name = "blogs/blogs_home.html"
