from django import forms

from App_main.models import *


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ['user']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', ]


