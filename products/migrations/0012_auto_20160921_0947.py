# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20160921_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='metatitle',
            field=models.CharField(default=1, max_length=120, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='metatitle',
            field=models.CharField(default=1, max_length=120, verbose_name='title'),
            preserve_default=False,
        ),
    ]
