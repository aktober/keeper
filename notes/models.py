from django.contrib.auth.models import User
from django.db import models
from django.forms import Textarea
from django.utils.datetime_safe import datetime


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Note(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    all_tags = models.ManyToManyField(Tag, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ': ' + self.text + ' ' + str(self.date)

    def save(self, *args, **kwargs):
        self.date = datetime.now()
        super(Note, self).save(*args, **kwargs)
