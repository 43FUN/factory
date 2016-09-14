from django.shortcuts import render

# Create your views here.


def chamfering(request):
    return render(request, 'chamfering.html')


def welding(request):
    return render(request, 'welding.html')


def plasmacutting(request):
    return render(request, 'plasmacutting.html')


def metallsawing(request):
    return render(request, 'metallsawing.html')
