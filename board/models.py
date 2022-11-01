import logging

from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=256, blank=True)
    create_date = models.DateTimeField('Create Time', auto_now=True, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title