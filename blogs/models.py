from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    excerpt = models.TextField(blank=False, null=True)
    featured_image = models.ImageField(default='default_featured_image.jpg',
                                       upload_to='featured_images')

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
