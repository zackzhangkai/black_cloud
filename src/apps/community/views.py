from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from apps.community.models import Topic, Comment, StarUser, UserScore
from django.db.models import F
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage


@login_required
def topic_list(request):
    """返回topic列表"""
    uid = request.user.id
    current_page = 1 if not request.GET.get('current_page') else request.GET.get('current_page')
    topics = Topic.objects.filter().order_by("date")
    paginator = Paginator(object_list=topics, per_page=10)
    try:
        page = paginator.page(current_page)
    except EmptyPage as e:
        # record meaningless request
        return HttpResponse('暂时没有话题')
    return


@login_required
def topic_details(request):
    """查看topic详情"""

    uid = request.user.id
    topic_id = request.POST.get('topic_id')
    topic_details = Topic.objects.filter(id=topic_id)
    comments = Comment.object.filter(topic_id=topic_id).order_by("date")
    return


@login_required
def create_topic(request):
    """创建topic"""
    user = request.user
    article = request.POST.get('article')
    title = request.POST.get('title')
    Topic.objects.create(user=user, article=article, title=title)
    update_score(user, 10)
    return HttpResponse('create-success')


@login_required
def create_comment(request):
    """发布评论"""
    user = request.user
    comment = request.POST.get('comment')
    topic_id = request.POST.get('topic_id')
    Comment.objects.create(user=user, comment=comment, topic_id=topic_id)
    update_score(user, 5)
    return HttpResponse('create-success')


@login_required
def create_star(request):
    """点赞"""
    community_id = request.POST.get('community_id')
    is_topic = request.POST.get('is_topic')
    if is_topic:
        topic = Topic.objects.get(id=community_id)
        topic.star.update(star=F('star') + 1)
    else:
        comment = Comment.objects.get(id=community_id)
        comment.star.update(star=F('star') + 1)

    StarUser.objects.create(user=request.user, community_id=community_id)
    update_score(request.user, 1)
    return HttpResponse('star-success')


@login_required
def delete_topic(request):
    user = request.user
    topic_id = request.POST.get('topic_id')
    u = Topic.objects.get(id=topic_id, user=user)
    u.delete()
    return HttpResponse('delete-success')


@login_required
def delete_comment(request):
    user = request.user
    topic_id = request.POST.get('comment_id')
    u = Topic.objects.get(id=topic_id, user=user)
    u.delete()
    return HttpResponse('delete-success')


@login_required
def leaderboard(request):
    leaders = UserScore.objects.filter().order_by("score")[:10]
    return leaders


def update_score(user, score):
    user_score = UserScore.objects.filter(user=user)
    if user_score.exists():
        UserScore.score.update(star=F('score') + score)
    else:
        UserScore.objects.create(user=user, score=score)
