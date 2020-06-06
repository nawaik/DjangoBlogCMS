from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(blank=True, upload_to='profiel/')

    def __str__(self):
        return self.username
