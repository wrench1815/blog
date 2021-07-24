from django.db import models
from ckeditor.fields import RichTextField


# Changelog Model
class ChangelogsModel(models.Model):
    """Model definition for ChangelogsModel."""
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
        """Meta definition for changelogsModel."""

        verbose_name = 'Changelog'
        verbose_name_plural = 'Changelogs'

    def __str__(self):
        """Unicode representation of changelogsModel."""
        return self.version_title
