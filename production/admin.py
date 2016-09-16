from django.contrib import admin
from production.models import Gallery

# Register your models here.


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ['file']
    list_filter = ['date']
    list_display = ['file', 'date']
