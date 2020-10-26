from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.timeline, name='timeline'),
    url(r'^upload/', views.post_upload, name='post_upload'),
    url(r'^post/<int:pk>/', views.post, name='post')
]