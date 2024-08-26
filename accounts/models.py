from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager  # Assuming your manager is in a file named managers.py

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=100,unique=False)
    user_bio = models.TextField(max_length=50,null=True,default=None)
    user_profile_image = models.ImageField(upload_to='profile_image', blank=True,default='profile_image/default.jpg')



    objects = UserManager()

    def __str__(self):
        return self.username
