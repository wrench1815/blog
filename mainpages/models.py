from django.db import models
from ckeditor.fields import RichTextField


# Changelog Model
class ChangelogsModel(models.Model):
    """Model definition for ChangelogsModel."""

    version_title = models.CharField(max_length=100)
    version_description = RichTextField()

    class Meta:
        """Meta definition for changelogsModel."""

        verbose_name = 'Changelog'
        verbose_name_plural = 'Changelogs'

    def __str__(self):
        """Unicode representation of changelogsModel."""
        return self.version_title
