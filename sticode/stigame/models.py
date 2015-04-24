from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StiGameNews(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    postedOn = models.DateTimeField()
    author = models.OneToOneField(User)

class StiGameRelease(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField()
    version = models.CharField(max_length=255)
    date = models.DateTimeField()