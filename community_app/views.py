from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from community_app.models import Topic, Comment, StarUser
from event_center_app.models import Event
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
def comments(request):
    """展示所有主题"""
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        article = request.POST.get("article")
        models.Topic.objects.create(user=user, title=title, article=article)
        t_objs = models.Topic.objects.all()
        return render(request, 'community_app/topic_list.html',
                      context={
                          't_objs': t_objs
                      }
        )
    else:
        t_objs = Topic.objects.all()
        return render(request, 'community_app/comments.html',
                  context={
                      't_objs': t_objs
                  }
        )


@login_required
def view_this_topic(request):
    """查看主题"""
    topic_id = request.GET.get("topic_id")
    t_objs = Topic.objects.filter(id=topic_id).first()
    print('nononon')
    print(t_objs)
    title = t_objs.title
    article = t_objs.article
    print(title)
    print(article)
    return render(request, 'community_app/topic_info.html',
                  context={
                      'title': title,
                      'article': article,
                  }
                  )

@login_required
def star_this_topic(request):
    """给主题点赞"""

    topic_id = request.GET.get('topic_id')
    action_user_id = request.GET.get('action_user_id')
    t_obj = Topic.objects.filter(id=topic_id).first()
    t_obj.star = t_obj.star + 1
    t_obj.save()
    u_obj = User.objects.filter(id=action_user_id).first()

    long_str = '%s 刚刚为 %s 点亮了一下哦～' %(u_obj.username, t_obj.title)
    e = Event.objects.create(subject=long_str)
    e.save()
    print(u_obj.username)

    print(topic_id)
    print(action_user_id)
    print('!!!')
    return redirect('community_app:show_topics')


