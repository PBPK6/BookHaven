from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_s = models.URLField(null=True, blank=True)
    image_m = models.URLField(null=True, blank=True)
    image_l = models.URLField(null=True, blank=True)

class userbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)