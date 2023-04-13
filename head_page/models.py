# tweet/models.py
from django.db import models
from users.models import UserModel


# Create your models here.
class headModel(models.Model):
    class Meta:
        db_table = "head"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)