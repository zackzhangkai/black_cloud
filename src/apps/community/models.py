from django.db import models
from django.contrib.auth.models import User


class Community(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=False)
    star = models.IntegerField()


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    article = models.TextField(null=False)
    title = models.CharField(max_length=80, null=False)
    star = models.IntegerField()
