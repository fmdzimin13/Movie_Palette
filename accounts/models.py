from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    personal_color = models.CharField(max_length=50, default='')
    color_code = models.CharField(max_length=50, default='')
