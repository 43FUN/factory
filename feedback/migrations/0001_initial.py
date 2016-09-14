# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('text', models.TextField(max_length=500)),
                ('file', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]