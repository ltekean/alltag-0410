from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "all_users"

    nickname = models.CharField(max_length=20, default="None")
    # profile_img = models.ImageField(null=True, upload_to="", blank=True)
    my_image = models.FileField("이미지 파일 등록", null=True, blank=True, upload_to="")
