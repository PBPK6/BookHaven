from django.db import models

class Book(models.Model):
    isbn = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_s = models.URLField(null=True, blank=True)
    image_m = models.URLField(null=True, blank=True)
    image_l = models.URLField(null=True, blank=True)

class userItem(models.Model):
    isbn = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    image_s = models.URLField(null=True, blank=True)
    image_m = models.URLField(null=True, blank=True)
    image_l = models.URLField(null=True, blank=True)