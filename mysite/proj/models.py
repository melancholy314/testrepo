from django.db import models
from django.urls import reverse
# Create your models here.

class spektakl(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    nazvanie = models.CharField(max_length=50)

class mesta(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    spektakl = models.CharField(max_length=50)
    sektor = models.CharField(max_length=50)
    mesto = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    sms = models.IntegerField(default=0)
    time = models.CharField(max_length=50)


