# Generated by Django 3.2.5 on 2021-07-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0004_alter_changelogsmodel_version_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='changelogsmodel',
            name='version_type',
            field=models.CharField(choices=[('Beta', 'Beta'), ('Major', 'Major'), ('Patch', 'Patch')], default='Beta', max_length=5),
        ),
    ]
