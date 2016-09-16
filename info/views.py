from django.shortcuts import render

# Create your views here.


def info(request):
    return render(request, 'info.html')


def company_card(request):
    return render(request, 'company_card.html')
