# Generated by Django 2.1.7 on 2019-09-21 06:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_center_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='involves_user',
        ),
        migrations.AddField(
            model_name='event',
            name='involves_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
