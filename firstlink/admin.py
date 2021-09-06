from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)  # 在Django admin里加入Question表
admin.site.register(Choice)
