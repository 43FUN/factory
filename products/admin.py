from django.contrib import admin
from products.models import Products, Category

# Register your models here.


@admin.register(Category)
class Category(admin.ModelAdmin):
    fields = ['name',
              'file',
              'seotitle',
              'seodescription'
              ]
    list_display = ['name']


@admin.register(Products)
class Products(admin.ModelAdmin):
    fields = ['name',
              'text',
              'file',
              'category',
              'seotitle',
              'seodescription'
              ]
    list_display = ['name', 'category']
    list_filter = ['category']

