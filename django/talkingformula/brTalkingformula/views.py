from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Circuito
from .models import Corrida
from .models import Piloto
from .models import PilotoEquipa
from .models import Equipa
from .models import Construtor


# Create your views here.

def index(request):
    template = loader.get_template('brTalkingformula/index.html')
    context = {
      
    }
    return HttpResponse(template.render(context, request))

def pilotos(request):
    template = loader.get_template('brTalkingformula/pilotos.html')
    items = Piloto.objects.order_by('nome')[0:]
    context = {
        'pilotos':items
    }

    return HttpResponse(template.render(context, request))

"""
def resultadoss(request):
    template = loader.get_template('brTalkingformula/resultados.html')
    items = Piloto.objects.order_by('nome')[0:]
    context = {
        'pilotos':items
    }

    return HttpResponse(template.render(context, request))
"""
    
def corridas(request):
    template = loader.get_template('brTalkingformula/corridas.html')
    items = Corrida.objects.order_by('ronda')[0:]                       #lista das corridas


    context = {
        'corridas': items,
    }
    return HttpResponse(template.render(context, request))

def circuitos(request):
    template = loader.get_template('brTalkingformula/circuitos.html')
    items = Corrida.objects.order_by('circuitoid')[0:]
    context = {
        'circuitos':items
    }
    return HttpResponse(template.render(context, request))

