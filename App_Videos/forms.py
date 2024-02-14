from django import forms
from App_Videos.models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            'comment': 'Comment',
        }
        