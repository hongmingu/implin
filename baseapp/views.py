from django.shortcuts import render, redirect, reverse
from relation.models import *
from object.models import *
from object.numbers import *
from notice.models import *
from django.db.models import Q
from django.db import transaction
import uuid

from django.utils.timezone import now, timedelta

# Create your views here.

def user_profile(request, user_username):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = None
            try:
                chosen_user = User.objects.get(userusername__username=user_username)
            except:
                return render(request, '404.html')
            if chosen_user is not None:
                following = None
                if Follow.objects.filter(user=request.user, follow=chosen_user).exists():
                    following = True

                return render(request, 'baseapp/user_profile.html', {'chosen_user': chosen_user, 'following': following})
        else:
            user = None
            try:
                chosen_user = User.objects.get(userusername__username=user_username)
            except:
                return render(request, '404.html')
            if chosen_user is not None:
                following = None
                return render(request, 'baseapp/user_profile.html',
                              {'chosen_user': chosen_user, 'following': following})

def create_new(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = None
                description = None
                has_another_profile = False
                profile_name = None

                if form.cleaned_data['whose'] == 'other':
                    has_another_profile = True
                    profile_name = form.cleaned_data['name']
                    profile_name = profile_name.strip()
                if form.cleaned_data['title'] == 'on':
                    title = form.cleaned_data['title_content']
                    title = title.strip()
                if form.cleaned_data['description'] == 'on':
                    description = form.cleaned_data['description_content']
                    description = description.strip()
                uuid_made = uuid.uuid4().hex
                post = Post.objects.create(user=request.user,
                                           title=title,
                                           description=description,
                                           has_another_profile=has_another_profile,
                                           uuid=uuid_made,
                                           is_open=False)
                post_first_check = PostFirstCheck.objects.create(post=post)
                post_like_count = PostLikeCount.objects.create(post=post)
                post_comment_count = PostCommentCount.objects.create(post=post)
                post_follow_count = PostFollowCount.objects.create(post=post)
                post_chat = PostChat.objects.create(post=post, before=None, kind=POSTCHAT_START, uuid=uuid.uuid4().hex)
                # 여기서 post unique constraint 처리 해주면 좋긴 하나 지금 하기엔 하고 싶지 않다.
                return redirect(reverse('baseapp:post_update', kwargs={'uuid': uuid_made}))
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect(reverse('baseapp:main_create_log_in'))
        return render(request, 'baseapp/create_new_first.html')


def post_update(request, uuid):
    if request.method == "GET":
        if request.user.is_authenticated:
            post = None
            try:
                post = Post.objects.get(uuid=uuid, user=request.user)

            except Post.DoesNotExist:
                return render(request, '404.html')
            just_created = {}
            if not post.postfirstcheck.first_checked:
                just_created['ok'] = 'on'
                post_first_check = post.postfirstcheck
                post_first_check.first_checked = True
                post_first_check.save()
            else:
                just_created['ok'] = 'off'
                if post.is_open:
                    just_created['current'] = 'open'
                else:
                    just_created['current'] = 'close'

            return render(request, 'baseapp/post_update.html', {'post': post, 'just_created': just_created})

def post(request, uuid):
    if request.method == "GET":
        post = None
        try:
            post = Post.objects.get(uuid=uuid)
        except:
            return render(request, '404.html')
        if post is not None:
            id_data = {}
            id_data['id'] = uuid
            return render(request, 'baseapp/post.html', {'id_data': id_data, 'post': post})

        return render(request, 'baseapp/post.html', )


def explore_feed(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'baseapp/user_feed.html')
        else:
            return redirect(reverse('baseapp:main_create_log_in'))


def note_all(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            try:
                with transaction.atomic():
                    notices_update = Notice.objects.filter(Q(user=request.user) & Q(checked=False)).update(
                        checked=True)
                    notice_count = request.user.noticecount
                    notice_count.count = 0
                    notice_count.save()
            except Exception as e:
                print(e)
                pass
            return render(request, 'baseapp/user_note.html')
        else:
            return redirect(reverse('baseapp:main_create_log_in'))


def search_all(request):
    if request.method == "GET":
        q = request.GET.get('q', None)
        word = {}
        word['q'] = q
        return render(request, 'baseapp/user_search_all.html', {'word': word})

def search_user(request):
    if request.method == "GET":
        q = request.GET.get('q', None)
        word = {}
        word['q'] = q
        return render(request, 'baseapp/user_search_user.html', {'word': word})

def search_post(request):
    if request.method == "GET":
        q = request.GET.get('q', None)
        word = {}
        word['q'] = q
        return render(request, 'baseapp/user_search_post.html', {'word': word})

def home(request):
    if request.method == "GET":

        return render(request, 'baseapp/home.html', )

def b_admin(request):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request, 'baseapp/b_admin.html')

        return render(request, '404.html', )


def b_admin_solo(request):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request, 'baseapp/b_admin_solo.html')

        return render(request, '404.html', )


def b_admin_group(request):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request, 'baseapp/b_admin_group.html')

        return render(request, '404.html', )

def b_admin_group_edit(request, uuid):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request, 'baseapp/b_admin_group_edit.html', {'id': uuid})

        return render(request, '404.html', )


def b_admin_solo_edit(request, uuid):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request, 'baseapp/b_admin_solo_edit.html', {'id': uuid})

        return render(request, '404.html', )


def b_admin_member(request):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request, 'baseapp/b_admin_member.html')

        return render(request, '404.html', )


from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt


def pay_charge(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            q = request.GET.get('q', None)
            if not q.isdigit():
                return render(request, '404.html')

            # What you want the button to do.
            user_id = request.user.username # 이거 데이터베이스에서 중복값 없도록 해야 한다. 여기 수정해야함.
            paypal_dict = {
                "business": "ghdalsrn2sell@gmail.com", # 판매자 계정 잘 써야 한다.
                "amount": q,
                "item_name": "name of the item",
                "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
                "return": request.build_absolute_uri(reverse('baseapp:pay_return')),
                "cancel_return": request.build_absolute_uri(reverse('baseapp:pay_cancel_return')),
                "custom": request.user.username,  # Custom command to correlate to some function later (optional)
            }
            print('reverse paypal-ipn: ' + reverse('paypal-ipn'))
            print('send uuid: '+ user_id)
            # Create the instance.
            form = PayPalPaymentsForm(initial=paypal_dict)
            context = {"form": form}
            return render(request, "baseapp/pay_charge.html", context)
# 여기서 paypal - profile - my selling tools - Instant payment notifications


@csrf_exempt
def pay_return(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "baseapp/pay_return.html")


@csrf_exempt
def pay_cancel_return(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "baseapp/pay_cancel_return.html")


@csrf_exempt
def pay_start(request):
    if request.method == "GET":
        if request.user.is_authenticated:
           return render(request, "baseapp/pay_start.html")

