# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-07 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_remove_note_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.Tag'),
        ),
    ]