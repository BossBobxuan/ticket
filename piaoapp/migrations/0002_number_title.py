# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('piaoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
