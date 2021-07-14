from django.urls import path
from .views import BlogPostsListView, BlogPostsDetailView

urlpatterns = [
    path('', BlogPostsListView.as_view(), name='blogs'),
    path('<slug:slug>-<int:pk>/',
         BlogPostsDetailView.as_view(),
         name='blogs-post-detail')
]
