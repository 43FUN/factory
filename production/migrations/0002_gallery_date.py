# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 09:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата'),
        ),
    ]
