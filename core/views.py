from django.shortcuts import render
from django.utils import timezone


def home(request):
    data = timezone.now()
    
    context = {
        'data_atual': data,
    }
    return render(request, 'core/index.html', context)


def sobre(request):
    context = {
        'titulo': 'Sobre'
    }
    return render(request, 'core/sobre.html', context)
