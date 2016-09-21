from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'category'
    name = models.CharField('Название', max_length=100)
    file = models.ImageField(
        upload_to="category", verbose_name='Изображение')
    seotitle = models.CharField(max_length=120, blank=True)
    seodescription = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'products'
    name = models.CharField('Название товара', max_length=100)
    text = models.TextField('Описание')
    file = models.ImageField(
        upload_to="product", verbose_name='Изображение', blank=True)
    category = models.ForeignKey(Category)
    seotitle = models.CharField(max_length=120, blank=True)
    seodescription = models.TextField(max_length=200, blank=True)
