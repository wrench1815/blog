from django.urls import path
from .views import home, about, contactMe

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contactMe, name='contactMe'),
    path('about/', about, name='about'),
]
