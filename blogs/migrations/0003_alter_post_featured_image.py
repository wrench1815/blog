# Generated by Django 3.2.2 on 2021-05-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='media/default_featured_image.jpg', upload_to='featured_images'),
        ),
    ]