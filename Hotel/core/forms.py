from django import forms
from .models import PostModel





class PostForm(forms.ModelForm):
    class Meta:
        model= PostModel
        fields = ("title", "head_image", "user", "category", "text")