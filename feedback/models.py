# -*- coding: utf-8 -*-

from django.db import models
import datetime

# Create your models here.


class Feedback(models.Model):
    class Meta():
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'feedback'
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=30)
    text = models.TextField(max_length=500)
    file = models.FileField(
        upload_to="files", verbose_name='Файл')
    date = models.DateTimeField(
        'Дата', default=datetime.datetime.now)

