from django.conf.urls import url, include
from django.contrib import admin

from . import views

#^$约束一个空字符串
urlpatterns = [
    url(r'^$', views.index),
]