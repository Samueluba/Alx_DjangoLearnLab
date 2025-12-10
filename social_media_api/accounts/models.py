from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField
    followers = models.ManyToManyField('self', symmetrical=False)

# Create your models here.
