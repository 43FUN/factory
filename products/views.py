from django.shortcuts import render

# Create your views here.


def accessories(request):
    return render(request, 'accessories.html')


def shell_ppu(request):
    return render(request, 'shell_ppu.html')


def system_odk(request):
    return render(request, 'system_odk.html')


def tubing_oc(request):
    return render(request, 'tubing_oc.html')


def tubing_pe(request):
    return render(request, 'tubing_pe.html')
