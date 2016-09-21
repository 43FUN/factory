from django.db import models
import datetime

# Create your models here.


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        db_table = 'gallery'
    file = models.ImageField(
        upload_to="gallery", verbose_name='Файл')
    date = models.DateTimeField(
        'Дата', default=datetime.datetime.now)
