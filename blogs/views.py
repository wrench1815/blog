from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Lists all Blog Posts from the DB Post
class BlogPostsListView(ListView):
    model = Post
    template_name = "blogs/blogs_home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Order Posts by Date Posted
    paginate_by = 4  # Paginate by 12 Posts per Page


# opens a Detailed Page of the Data for the Blog Post
class BlogPostsDetailView(DetailView):
    model = Post
    template_name = 'blogs/blogs_detail.html'
    context_object_name = 'post'
