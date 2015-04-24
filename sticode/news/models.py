from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    postedOn = models.DateTimeField()
    author = models.OneToOneField(User)
