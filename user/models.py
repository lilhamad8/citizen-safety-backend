from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    phone = models.IntegerField(null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    picture = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=200, blank=True)