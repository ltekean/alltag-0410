from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "all_users"

    nickname = models.CharField(max_length=20, default="None")
<<<<<<< HEAD
    profile_img = models.FileField(upload_to='../static/img/') # 마이페이지, 메인페이지에 보여줄 프로필 이미지 db
=======
    # profile_img = models.ImageField(null=True, upload_to="", blank=True)
>>>>>>> 294d29d (all_users 내 pofile_img db 주석처리)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followee")
