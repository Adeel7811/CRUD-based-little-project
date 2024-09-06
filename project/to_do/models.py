from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    time = models.TimeField(auto_now_add=False, null=True, blank=True)