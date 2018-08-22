from django.db import models
from imagekit.models import ImageSpecField # < import this
from imagekit.processors import ResizeToFill # < import this
from django.utils import timezone
import datetime 

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
