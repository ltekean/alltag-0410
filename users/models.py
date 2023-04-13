from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "all_users"

    nickname = models.CharField(max_length=20, default="None")
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followee")
