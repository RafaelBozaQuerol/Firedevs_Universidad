# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2021-08-27 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universidad', '0002_auto_20210827_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='carnet',
            field=models.CharField(default='88081208344', max_length=11),
        ),
        migrations.AddField(
            model_name='profesor',
            name='carnet',
            field=models.CharField(default='88081208344', max_length=11),
        ),
    ]
