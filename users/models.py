#user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "all_users"

    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    nickname = models.CharField(max_length=20, default='None')
   