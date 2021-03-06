from django.db import models
from imagekit.models import ImageSpecField # < import this
from imagekit.processors import ResizeToFill # < import this
from django.utils import timezone
from datetime import datetime, date, time, timedelta

class Post(models.Model):
    image = models.ImageField(upload_to="post_images") # Regular image field
    title = models.CharField(max_length=200)
    body = models.TextField()
    signature = models.CharField(max_length=140, default= 'JR')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)
