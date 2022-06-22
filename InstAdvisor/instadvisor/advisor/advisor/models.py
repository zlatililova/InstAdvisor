from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    execrpt = models.TextField()

    def __str__(self):
        return self.title

class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name = "email")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"