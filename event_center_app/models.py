from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):

    insert_time = models.DateTimeField(auto_now_add=True)
    involves_user = models.ManyToManyField(to=User)
    subject = models.CharField(max_length=80)








