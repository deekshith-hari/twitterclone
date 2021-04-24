from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
# Create your models here.
class Tweet(models.Model):
    body = models.TextField(max_length=140)
    likes = models.IntegerField(default=0)
    image = CloudinaryField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
