from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=90)#models.TextField()
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title + ': ' + self.text + ' ' + str(self.date)
