from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'email',
        'phone',
        'text',
        'file',
        'date',
    ]
    list_filter = ['date']
    list_display = ['name', 'email', 'date', 'text']
