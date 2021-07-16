from django.contrib import admin
from .models import ChangelogsModel


# Registering changelogsModel into admin
@admin.register(ChangelogsModel)
class ChangelogsModelAdmin(admin.ModelAdmin):
    '''Admin View for ChangelogsModel'''

    list_display = ('version_title', 'version_description')

    class Media:
        js = ['js/main.js']
