# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='file',
            field=models.ImageField(upload_to='media/imageg/', verbose_name='Ваше фото'),
        ),
    ]
