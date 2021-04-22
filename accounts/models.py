from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = CloudinaryField(blank=True)
    bio = models.TextField(default='')

    def __str__(self):
        return self.user.username
