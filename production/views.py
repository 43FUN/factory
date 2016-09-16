from django.shortcuts import render
from production.models import Gallery

# Create your views here.


def production(request):
    gallery = Gallery.objects.all
    return render(request, 'production.html', {'gallery': gallery})
