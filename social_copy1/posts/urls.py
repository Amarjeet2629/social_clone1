from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = 'posts'

urlpatterns = [
    url(r'^create/(?P<slug>[-\w]+)/$', views.PostCreate, name='post_create'),
    url(r'^delete/(?P<slug>[-\w]+)/(?P<pk>[0-9]+)/$', views.PostDelete, name='post_delete'),
    url(r'^by/(?P<username>[-\w]+)/$', views.UserPostDetail, name='user_post'),

]
