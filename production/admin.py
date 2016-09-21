from django.contrib import admin
from production.models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    fields = ['file']
    list_filter = ['date']
    list_display = ['file', 'date']
