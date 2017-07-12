from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, default='', blank=True)
    bio = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.user.username + ': ' + self.user.first_name + \
            ' ' + self.user.last_name
