# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-12 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_auto_20170408_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
