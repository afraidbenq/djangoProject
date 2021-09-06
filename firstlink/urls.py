from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
# 每个APP都要新增urls.py文件用于根据url调用app内的视图
