from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from community_app.models import Topic, Comment

# Create your views here.


@login_required
def show_topics(request):
    """展示所有主题"""
    t_objs = Topic.objects.all()
    return render(request, 'community_app/topic_list.html',
                  context={
                      't_objs': t_objs
                  })






