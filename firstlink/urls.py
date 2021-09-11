from django.urls import path

from . import views

app_name = 'firstlink'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/          http://127.0.0.1:8000/firstlink/1/
    path('1/<int:question_id>/', views.detail, name='detail'),  # 模板不是硬编码后，URL路径可以随意修改，
    # ex: /polls/5/results/  http://127.0.0.1:8000/firstlink/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/     http://127.0.0.1:8000/firstlink/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# 每个APP都要新增urls.py文件用于根据url调用app内的视图
