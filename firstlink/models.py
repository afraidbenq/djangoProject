from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 字符字段被表示为 CharField
    pub_date = models.DateTimeField('date published')  # 日期时间字段被表示为 DateTimeField

    def __str__(self):                 # Django python shell里面可调用
        return self.question_text

    def was_published_recently(self):  # Django python shell里面可调用
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 定义了一个关系，每个 Choice 对象都关联到一个 Question 对象
    choice_text = models.CharField(max_length=200)  # 设置最大字符长度为200
    votes = models.IntegerField(default=0)  # 设置默认值为0

    def __str__(self):
        return self.choice_text