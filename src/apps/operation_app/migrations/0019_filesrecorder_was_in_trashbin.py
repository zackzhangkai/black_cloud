# Generated by Django 2.1.7 on 2019-03-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_app', '0018_auto_20190314_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesrecorder',
            name='was_in_trashbin',
            field=models.BooleanField(default=False),
        ),
    ]