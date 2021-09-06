"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('firstlink/', include('firstlink.urls')),
    # path('gostock/', include('gostock.urls')),
    path('admin/', admin.site.urls),
    # 函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name。
    # route 是一个匹配 URL 的准则（类似正则表达式）
    # view 会调用这个特定的视图函数
    # kwargs 任意个关键字参数可以作为一个字典传递给目标视图函数
    # name 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。
]
