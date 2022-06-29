from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy

from App_login.models import CustomUser
from App_main.forms import StoryForm
from App_main.models import Story, Likes, Comments, Message


def likes_def(request, pk):
    this_story = Story.objects.get(id=pk)
    user = request.user
    already_liked = Likes.objects.filter(story_liked=this_story, user_liked=user)
    if not already_liked:
        like_post = Likes()
        like_post.story_liked = this_story
        like_post.user_liked = user
        like_post.save()
    else:
        already_liked.delete()
    return 'done'


def comment_def(request, pk, comment):
    this_story = Story.objects.get(id=pk)
    user = request.user
    comment_post = Comments()
    comment_post.user_commented = user
    comment_post.story_commented = this_story
    comment_post.comment = comment
    comment_post.save()
    return 'Done'


@login_required
def home(request):
    if request.method == 'POST' and 'like_btn' in request.POST:
        pk = request.POST.get('like')
        like_def = likes_def(request, pk)
    if request.method == 'POST' and 'comment_btn' in request.POST:
        pk = request.POST.get('comment_story')
        comment = request.POST.get('comment')
        comment_def(request, pk, comment)
    stories = Story.objects.all()
    if request.method == "POST" and 'msg_btn' in request.POST:
        r = request.POST.get('receiver')
        receiver = CustomUser.objects.get(username=r)
        message = request.POST.get('message')
        msg = Message()
        msg.sender = request.user
        msg.receiver = receiver
        msg.message = message
        msg.save()
    messages = Message.objects.all()
    print(messages)
    likes = Likes.objects.filter(user_liked=request.user)
    like_list = [x.story_liked_id for x in likes]
    comments = Comments.objects.all()
    comment_list = [x.story_commented_id for x in comments]
    content = {
        'stories': stories,
        'likes': like_list,
        'comment_list': comment_list,
        'comments': comments,
        'messages': messages,
    }
    return render(request, 'App_main/home.html', context=content)


def story(request):
    form = StoryForm()
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            this_form = form.save(commit=False)
            this_form.user = request.user
            this_form.save()
            return HttpResponseRedirect(reverse('App_main:home'))
    content = {
        'form': form
    }
    return render(request, 'App_main/upload_new_story.html', context=content)


