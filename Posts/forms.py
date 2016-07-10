from django.contrib.auth.models import User
from .models import Post, RichTextField
from django import forms

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'title'}))

    class Meta:
        model = Post
        fields = ['title', 'content']