from django.db import models
from users.models import UserModel


class WriteModel(models.Model):
    class Meta:
        db_table = "writes"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default="무제")
    content = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
