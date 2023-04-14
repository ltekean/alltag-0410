from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "all_users"

    nickname = models.CharField(max_length=20, default="None")
    profile_img = models.FileField(upload_to='../static/img/') # 마이페이지, 메인페이지에 보여줄 프로필 이미지 db
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followee")
