from django.urls import path
from .views import home, about, contactMe, changelogs, ContactForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contactMe, name='contactMe'),
    path('about/', about, name='about'),
    path('changelogs/', changelogs, name='site-changelogs'),
    path('contact_form/', ContactForm.as_view(), name='contact_form')
]
