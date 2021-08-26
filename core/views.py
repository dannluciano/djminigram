from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from django.utils import timezone


def home(request):
    data = timezone.now()
    
    context = {
        'data_atual': data,
        'titulo': 'Minha Pagina',
    }
    # template = loader.get_template('core/index.html')
    # return HttpResponse(template.render(context))
    

    return render(request, 'core/index.html', context)
