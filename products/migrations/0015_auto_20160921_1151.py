# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20160921_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='name',
        ),
    ]
