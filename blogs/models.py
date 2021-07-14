from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    post_tagline = models.CharField(
        max_length=100, default='This is a default Tagline, Change it')
    content = models.TextField(blank=True)
    excerpt = models.TextField(blank=False, null=True, max_length=200)
    slug = models.SlugField(null=False, editable=False, max_length=100)
    featured_image = models.ImageField(default='default_featured_image.jpg',
                                       upload_to='featured_images')

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {'slug': self.slug, 'pk': self.pk}
        return reverse('blog:blog-post', kwargs=kwargs)

    def save(self, *args, **kwargs):
        # if not self.slug:
        value = self.title
        self.slug = slugify(value)

        super().save(*args, **kwargs)
