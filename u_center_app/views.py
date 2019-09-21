from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from community_app.models import Topic, Comment, StarUser, UserScore

# Create your views here.


@login_required
def show_my_info(request):
    """展示当前用户信息"""
    user_id = request.user.id
    print('im-user')
    print(user_id)
    all_topic = Topic.objects.filter(user__pk=user_id)
    all_comment = Comment.objects.filter(user__pk=user_id)
    submit_cnt = len(all_topic)
    comment_cnt = len(all_comment)
    sub_star = 0
    for i in all_comment:
        sub_star += i.star
    com_star = 0
    for j in all_comment:
        com_star += j.star
    have_star = sub_star + com_star

    sended_star = StarUser.objects.filter(user__pk=user_id).first()
    try:
        if sended_star.sended_star:
            sended_star = sended_star.sended_star
    except:
        sended_star = 0

    return render(request, 'u_center_app/user_info.html',
                  context={
                      'submit_cnt': submit_cnt,
                      'comment_cnt': comment_cnt,
                      'sended_star': sended_star,
                      'have_star': have_star,
                           })


@login_required
def show_my_success(request):
    """展示当前用户成就"""

    user_id = request.user.id
    all_topic = Topic.objects.filter(user__pk=user_id)
    all_comment = Comment.objects.filter(user__pk=user_id)
    submit_cnt = len(all_topic)
    comment_cnt = len(all_comment)
    sub_star = 0
    for i in all_comment:
        sub_star += i.star
    com_star = 0
    for j in all_comment:
        com_star += j.star
    have_star = sub_star + com_star

    sended_star = StarUser.objects.filter(user__pk=user_id).first()
    try:
        if sended_star.sended_star:
            sended_star = sended_star.sended_star
    except:
        sended_star = 0

    max_val = max([submit_cnt, comment_cnt, have_star, sended_star])
    if max_val == 0:
        max_val = 10
    print('hi-attention %s'%((have_star+1)/max_val))

    degree_map = {
        0:'菜鸟',
        1:'青铜',
        2:'白银',
        3:'黄金',
        4:'铂金',
        5:'钻石',

    }

    return render(request, 'u_center_app/user_success.html',
                  context={
                      'max_val': max_val,
                      'yk': have_star, 'ykd':degree_map[have_star],'ykl':((have_star+1)/max_val)*200,
                      'zw': comment_cnt, 'zwd':degree_map[comment_cnt],'zwl':((comment_cnt+1)/max_val)*200,
                      'ly': have_star, 'lyd':degree_map[have_star],'lyl':((have_star+1/max_val))*200,
                      'hj': sended_star, 'hjd':degree_map[sended_star],'hjl':((sended_star+1/max_val))*200,

                  })





