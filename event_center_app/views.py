from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from event_center_app.models import Event

# Create your views here.


@login_required
def query_event(request):
    """查询是否有新的推送事件，若有，直接返回"""
    import datetime
    now_time = datetime.datetime.now()
    expiry_time = now_time-datetime.timedelta(seconds=10)
    print(expiry_time)
    # e = Event.objects.create(subject='hello')
    # e.save()
    new_event = Event.objects.filter(insert_time__gte=expiry_time).order_by('-insert_time').first()
    try:
        subject = new_event.subject
    except:
        subject = 'nothing'
    return JsonResponse({'subject': subject})


@login_required
def display_event(request):
    """展示所有事件"""

    e_objs = Event.objects.all().order_by('-insert_time')
    return render(request, 'event_center_app/event_center.html',
                  context={
                      'e_objs': e_objs,
                  })





