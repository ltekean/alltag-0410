from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "all_users"

    nickname = models.CharField(max_length=20, default="None")
    image = models.ImageField(upload_to="", null=True, blank=True)
    # profile_img = models.ImageField(null=True, upload_to="", blank=True)
