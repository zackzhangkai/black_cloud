# Generated by Django 2.1.7 on 2019-03-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_app', '0009_auto_20190308_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesrecorder',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]