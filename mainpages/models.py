from django.db import models
from ckeditor.fields import RichTextField


# Changelog Model
class ChangelogsModel(models.Model):
    '''Model definition for ChangelogsModel.'''
    VERSION_TYPE = (
        ('Beta', 'Beta'),
        ('Major', 'Major'),
        ('Patch', 'Patch'),
    )

    version_title = models.CharField(max_length=100)
    version_description = RichTextField()
    version_type = models.CharField(max_length=5,
                                    choices=VERSION_TYPE,
                                    default='Beta')

    class Meta:
        '''Meta definition for ChangelogsModel'''

        verbose_name = 'Changelog'
        verbose_name_plural = 'Changelogs'

    def __str__(self):
        '''Unicode representation of ChangelogsModel.'''
        return self.version_title


class ContactForm(models.Model):
    '''Model Definitions for Contact Form'''
    full_name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False, )
    was_readed = models.BooleanField(default=False)

    class Meta:
        '''Meta definition for ContactForm'''
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'

    def __str__(self):
        '''Unicode representation of ContactForm'''
        return self.full_name
