from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    nationality = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    trainName = models.CharField(max_length=40)
    berth = models.CharField(max_length=20)
    classs = models.CharField(max_length=20)
    fromm = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
