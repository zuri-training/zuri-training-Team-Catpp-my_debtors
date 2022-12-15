from .models import *
from django import forms

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["body", "topics"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]