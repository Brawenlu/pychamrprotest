from django.db import models


# Create your models here.

class Zhuce(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=32)
    sex = models.CharField(max_length=20)
    married = models.CharField(max_length=20)
    hobby = models.CharField(max_length=20)
    introduction = models.CharField(max_length=256)
    age = models.CharField(max_length=10)