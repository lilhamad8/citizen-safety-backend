from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    phone = models.IntegerField(unique=True, null=True)
    username = models.EmailField(unique=True, blank=True, null=True, max_length=254,)
    email = models.EmailField(unique=True, max_length=254,)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    date_joined = models.DateTimeField(default=timezone.now)
    picture = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.first_name+' '+self.last_name