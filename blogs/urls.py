from django.urls import path
from .views import BlogPostsListView

urlpatterns = [
    path('', BlogPostsListView.as_view(), name='blogs'),
]
