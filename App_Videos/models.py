from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Video(models.Model):
    video_code = models.CharField(max_length=264)
    title = models.CharField(max_length=264)
    description = models.TextField(max_length=1600)
    thumbnail = models.ImageField(upload_to='videos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-views','-updated_at', '-created_at', 'title']

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='commented_video', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment
    

class Likes(models.Model):
    user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='liked_video', on_delete=models.CASCADE)

    