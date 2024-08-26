# from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class Blog(models.Model):
    title = models.CharField(max_length=100,default='UNTITLED')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    caption = models.TextField()
    likes = models.IntegerField(default=0)
    shared_post = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True,null=True)
    objects = BlogManager()
    admin_objects=models.Manager()

    def __str__(self):
        return f'{self.caption[:40]}...'
class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    objects = CommentManager()
    admin_objects=models.Manager()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username}: {self.comment[:20]}...'
