"""POsts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Posts import views

urlpatterns = [
   # url(r'^main/', ),
     url(r'^view$', view=views.Posts.as_view(), name='posts_list'),
     url(r'^view/(?P<pk>[0-9]+)', view=views.Post_Detail.as_view(), name='posts_detail'),
     url(r'^add', view=views.Post_Create.as_view(), name='post_create'),
     url(r'^create/', view=views.Post_Create_Ajax, name='post_create'),
     url(r'^update/(?P<pk>[0-9]+)', view=views.Post_Update.as_view(), name='post_update'),
     url(r'^delete/(?P<pk>[0-9]+)', view=views.Post_Delete.as_view(), name='post_delete'),
     url(r'^register', view=views.UserFormView.as_view(), name='register'),
     url(r'^login', view=views.UserLogin.as_view(), name='login'),
     url(r'^logout', view=views.logout, name='logout')
]
