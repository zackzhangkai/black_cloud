from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """社区话题表"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    article = models.TextField(null=False)
    title = models.CharField(max_length=80, null=False)
    star = models.IntegerField(default=0)


class Comment(models.Model):
    """话题评论表"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=False)
    star = models.IntegerField(default=0)
    topic_id = models.ForeignKey(to=Topic, on_delete=models.CASCADE)


class StarUser(models.Model):
    """用户点赞关系表"""
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    community_id = models.IntegerField()


