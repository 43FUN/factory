#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Feedback(models.Model):
    class Meta():
        db_table='feedback'
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=30)
    text = models.TextField(max_length=500)
    file = models.ImageField('Прикрепить изображение')