from django.urls import path
from .views import home, about, contactMe, changelogs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contactMe, name='contactMe'),
    path('about/', about, name='about'),
    path('changelogs/', changelogs, name='site-changelogs')
]
