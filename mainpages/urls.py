from django.urls import path
from .views import home, about, contactMe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contactMe, name='contactMe'),
    path('about/', about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
