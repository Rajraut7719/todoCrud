from enum import _auto_null, auto
from statistics import mode
from django.db import models

# Create your models here.
class User(models.Model):
    title=models.CharField(max_length=70)
    project=models.CharField(max_length=70)
    description=models.TextField(max_length=90)
    # time=models.DateTimeField(auto_now_add=True)