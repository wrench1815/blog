from django.contrib import admin
from .models import ChangelogsModel
from django.utils.html import format_html


# Registering changelogsModel into admin
@admin.register(ChangelogsModel)
class ChangelogsModelAdmin(admin.ModelAdmin):
    '''Admin View for ChangelogsModel'''

    list_display = ('version_title', 'versionType')

    @admin.display(description='Version Type')
    def versionType(self, obj):
        if obj.version_type == 'Beta':
            return format_html(
                '<div class="text-white font-weight-bold d-inline-block py-1 px-3" style="background-image: linear-gradient(310deg,#f53939,#fac60b); border-radius: .5rem;">{}</div>',
                obj.version_type)

        elif obj.version_type == 'Major':
            return format_html(
                '<div class="text-white font-weight-bold d-inline-block py-1 px-3" style="background-image: linear-gradient(310deg,#17ad37,#84dc14); border-radius: .5rem;">{}</div>',
                obj.version_type)
        else:
            return format_html(
                '<div class="text-white font-weight-bold d-inline-block py-1 px-3" style="background-image: linear-gradient(310deg,#2152ff,#02c6f3); border-radius: .5rem;">{}</div>',
                obj.version_type)
