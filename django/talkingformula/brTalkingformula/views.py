from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import numpy as np

from .models import Circuito
from .models import Corrida
from .models import Piloto
from .models import PilotoEquipa
from .models import Equipa
from .models import Construtor
from .models import Noticia
from .models import Resultados
from .models import Epoca
from .models import ResultadoPontos

# Create your views here.

def index(request):
    template = loader.get_template('brTalkingformula/index.html')
    ultima_noticia = Noticia.objects.latest('criadoem')
    ultima_epoca = Epoca.objects.order_by('-ano')[0]

    ultimas_corridas = Corrida.objects.order_by('-epoca_ano').order_by('-ronda')

    resultados = []
    for corrida in ultimas_corridas:
        # Retrieve the Resultados objects for the Corrida object
        resultados_corrida = corrida.resultados_set.all()
        # Append the Resultados objects to the list
        resultados.extend(resultados_corrida)

    
    ultima_corrida = ultimas_corridas[0]
    ultimo_resultados = Resultados.objects.filter(corrida_ronda = ultima_corrida.ronda).order_by('posfinal')[:3]
    
    

    context = {
        'noticia': ultima_noticia,
        'ultimo_resultado': ultimo_resultados,
        'stadings' : resultados
    }
    return HttpResponse(template.render(context, request))

def pilotos(request):
    template = loader.get_template('brTalkingformula/pilotos.html')
    items = Piloto.objects.order_by('nome')[0:]
    context = {
        'pilotos':items
    }

    return HttpResponse(template.render(context, request))

def get_pontos(posfinal):
  # Query the Pontosresultados model to get the pontos value for the given posfinal value
  try:
    pontosresultado = ResultadoPontos.objects.get(posfinal=posfinal)
    return pontosresultado.pontos
  except ResultadoPontos.DoesNotExist:
    return 0

def resultados(request):
    template = loader.get_template('brTalkingformula/resultados.html')
    
    epoca = Epoca.objects.order_by('-ano')[0]
    ultimas_corridas = Corrida.objects.filter(epoca_ano = epoca).order_by('-ronda')
    
    #quero dicionário com {piloto, pontos;
    #                           }
 
    resultados = []
    for corrida in ultimas_corridas:
        resultados_corrida = corrida.resultados_set.all()
        resultados.extend(resultados_corrida)
    
    standings = [1,1]
    for piloto in Piloto.objects.all():
        soma = 0
        for resultado in resultados:
            if (piloto.pilotoid==resultado.piloto_pilotoid.pilotoid):
                soma = soma + get_pontos(resultado.posfinal)
        standings = np.vstack([standings, [piloto, int(soma)]]) 

    standings = standings[1:]
    standings = standings[(standings[:, 1]).argsort()[::-1]]


    context = {
        'standings': standings
    }

    return HttpResponse(template.render(context, request))

    
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


def noticias(request):
  noticias = Noticia.objects.all()
  return render(request, 'noticias.html', {'noticias': noticias})
