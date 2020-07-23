import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


#模型一问题
class Question(models.Model):


    # 创建的字段
    question_text = models.CharField(max_length=200) #问题描述
    pub_date = models.DateTimeField('date published') #创建时间

    def __str__(self):
        return self.question_text


    def was_published_recently(self):
          now = timezone.now()  #现在的时间
          return now - datetime.timedelta(days=1) <= self.pub_date <= now  #规定时间在现在到未来一天这个时间段


#模型二选项
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) # 选项描述
    votes = models.IntegerField(default=0) #投票数

    def __str__(self):
        return self.choice_text