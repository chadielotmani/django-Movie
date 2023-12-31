# models.py
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.URLField()
    overview = models.TextField()
    release_date = models.DateField()

def __str__(self):
    return self.title