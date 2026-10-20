from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db.models import Avg
import datetime
# Create your models here.

class User(AbstractUser):
    is_reviewer = models.BooleanField(default=False)
    is_blogger = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=False)
    #avatar = models.ImageField(default='stockAvatar.jpg', upload_to='profile_images')
    email = models.EmailField(max_length=255, unique=True, null=False)
    joined_date = models.DateField(auto_now_add=True, null=False)
    password = models.CharField(max_length=255, null=False)


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=False)
    pen_name = models.CharField(max_length=255)
    joined_date = models.DateField(auto_now_add=True, null=False)




