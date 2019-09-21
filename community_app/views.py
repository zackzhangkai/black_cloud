from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from community_app.models import Topic, Comment
from community_app import models

@login_required
def show_topics(request):
    """展示所有主题"""
    if request.method == 'POST':
        user= request.user
        title = request.POST.get("title")
        article= request.POST.get("article")
        models.Topic.objects.create(user=user, title=title, article=article)
        t_objs = models.Topic.objects.all()
        return render(request, 'community_app/topic_list.html',
                      context={
                          't_objs': t_objs
                      })
    else:
        t_objs = Topic.objects.all()
        return render(request, 'community_app/topic_list.html',
                  context={
                      't_objs': t_objs
                  })

@login_required
def show_comments(request):
    """展示所有主题"""
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        article = request.POST.get("article")
        models.Topic.objects.create(user=user, title=title, article=article)
        t_objs = models.Topic.objects.all()
        return render(request, 'community_app/show_comments.html',
                      context={
                          't_objs': t_objs
                      }
        )
    else:
        t_objs = Topic.objects.all()
        return render(request, 'community_app/show_comments.html',
                  context={
                      't_objs': t_objs
                  }
        )






