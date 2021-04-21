from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    body = models.CharField(max_length=140)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete = models.CASCADE)
