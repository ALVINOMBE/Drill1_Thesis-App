from django import forms
from .models import Thesis, Comment

class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['title', 'author', 'description', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
