# Generated by Django 3.2.6 on 2021-08-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0006_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='was_readed',
            field=models.BooleanField(default=False),
        ),
    ]