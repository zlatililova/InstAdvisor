
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to="media", blank=True)
    time_created = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class ExtendUser(AbstractUser):
    email = models.EmailField(
        blank=False, max_length=255, verbose_name="email")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
