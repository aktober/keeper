from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    tags = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ': ' + self.text + ' ' + str(self.date)

    def save(self, *args, **kwargs):
        self.date = datetime.now()
        super(Note, self).save(*args, **kwargs)
