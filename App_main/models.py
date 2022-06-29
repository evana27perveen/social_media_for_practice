from django.db import models

from App_login.models import CustomUser


class Story(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='story_author')
    picture = models.ImageField(upload_to='stories')
    story = models.TextField()
    post_date = models.DateField(auto_now=True)


class Likes(models.Model):
    user_liked = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_who_liked')
    story_liked = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='story_liked')
    date_liked = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    user_commented = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_who_commented')
    story_commented = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='story_commented')
    comment = models.TextField()
    date_commented = models.DateTimeField(auto_now=True)


class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)
