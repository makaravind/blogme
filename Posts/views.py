from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import *
from .models import Post
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import UserForm, UserLoginForm, CreatePostForm

from .serializers import Post_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets

class Posts(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        posts_list = Post.objects.all().order_by('-updated')
        return posts_list


class Post_Detail(DetailView):
    model = Post


@login_required
def Post_Create_Ajax(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        response_data = {}

        new_post = Post(title=title, content=content, author=request.user)
        new_post.save()

        response_data['result'] = 'Create post successful!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

class Post_Create(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = CreatePostForm
    template_name = 'posts/post_form.html'

    # def post(self, request, *args, **kwargs):
    #     title = request.POST['title']
    #     content = request.POST['content']
    #     author = request.POST['author']
    #
    #     Post.objects.create()

    def get_initial(self):
        return {'author': self.request.user}

    def get_success_url(self):
        return reverse('posts_list')


class Post_Update(LoginRequiredMixin, UpdateView):
    login_url = 'login'

    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('posts_list')


class Post_Delete(LoginRequiredMixin, DeleteView):
    login_url = 'login'

    model = Post

    def get_success_url(self):
        return reverse('posts_list')


class UserFormView(View):

    form_class = UserForm
    template_name = 'posts/registration_form.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #to create a new user
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned to save to DB
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns if user credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    # accesing request.user.usernam
                    return redirect('/posts/view')

        return render(request, self.template_name, {'form': form})


class UserLogin(View):

    form_class = UserLoginForm
    template_name = 'posts/User_Login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # to verify a user
    def post(self, request):

        # cleaned to save to DB
        username = request.POST['username']
        password = request.POST['password']

        # returns if user credentials are correct
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # accesing request.user.usernam
                return redirect('/posts/view')
        else :
            return redirect('/posts/login')


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('login')


# API
@api_view(['GET'])
def MyPostList(request, author):
    if request.method == 'GET':
        author_posts = Post.objects.all().filter(author=author)
        serializer = Post_Serializer(author_posts, many=True)
        return Response(serializer.data)


