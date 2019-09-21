import datetime
from datetime import timezone
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from community_app.models import Topic

# Create your views here.


@login_required
def show_top_list(request):
    """展示热度排行"""

    now = timezone.now()
    start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)

    today_t_objs = Topic.objects.filter(date__gt=start).order_by('-star')
    if today_t_objs:
        today_t_objs = today_t_objs[:5]

    history_t_objs = Topic.objects.filter(date__gt=start).order_by('-star')
    if history_t_objs:
        history_t_objs = history_t_objs[:5]

    return render(request, 'hotlist_app/hot_list.html',
                  context={
                      'today_t_objs': today_t_objs,
                      'history_t_objs': history_t_objs
                  })




