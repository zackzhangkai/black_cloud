# Generated by Django 2.1.7 on 2019-03-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesrecorder',
            name='upload_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
