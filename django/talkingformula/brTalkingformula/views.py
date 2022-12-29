from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import numpy as np
from django.db.models import Sum


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
from .models import Comentario

from .forms import ComentarioForm

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


def circuito(request, circuitoid):
    template = loader.get_template('brTalkingformula/circuito.html')
    items = Circuito.objects.get(circuitoid = circuitoid)                       #lista dos circuitos
    context = {
        'circuito':items
    }

    return HttpResponse(template.render(context, request))



def pilotosDetails(request, pilotoid):
    template = loader.get_template('brTalkingformula/piloto_detalhes.html')
    

    try:
        piloto = Piloto.objects.get(pilotoid = pilotoid)
        context = {
            'piloto' : piloto
            }
    except Piloto.DoesNotExist:
        raise Http404("Guitar does not exist")
    return HttpResponse(template.render(context, request))

    


def get_pontos(posfinal):
  # Query the Pontosresultados model to get the pontos value for the given posfinal value
  try:
    pontosresultado = ResultadoPontos.objects.get(posfinal=posfinal)
    return pontosresultado.pontos
  except ResultadoPontos.DoesNotExist:
    return 0

def resultadosPilotos(request, epoca_ano=Epoca.objects.first().ano):
    template = loader.get_template('brTalkingformula/resultados.html')
    
    epocas = Epoca.objects.all()
    ultimas_corridas = Corrida.objects.filter(epoca_ano = epoca_ano).order_by('-ronda')
    
    
 
    resultados = []
    for corrida in ultimas_corridas:
        resultados_corrida = corrida.resultados_set.all()
        resultados.extend(resultados_corrida)
    
    standings = [1,1]

    for pilotoEquipa in PilotoEquipa.objects.all():
        soma = 0
        for resultado in resultados:
            if (pilotoEquipa.piloto_pilotoid.pilotoid==resultado.piloto_pilotoid.pilotoid):
                soma = soma + get_pontos(resultado.posfinal)
        standings = np.vstack([standings, [pilotoEquipa, soma]]) 

    standings = standings[1:]
    standings = standings[(standings[:, 1]).argsort()[::-1]]


    context = {
        'standings': standings,
        'epocas' : epocas,
    }

    return HttpResponse(template.render(context, request))

def resultadosConstrutores(request, epoca_ano=Epoca.objects.first().ano):
    template = loader.get_template('brTalkingformula/resultados.html')
    
    epocas = Epoca.objects.all()
    ultimas_corridas = Corrida.objects.filter(epoca_ano = epoca_ano).order_by('-ronda')
    
    for pilotoEquipa in PilotoEquipa.objects.all():
        soma = 0
        for resultado in resultados:
            if (pilotoEquipa.piloto_pilotoid.pilotoid==resultado.piloto_pilotoid.pilotoid):
                soma = soma + get_pontos(resultado.posfinal)
        standings = np.vstack([standings, [pilotoEquipa, soma]]) 
    
    resultados = []
    for corrida in ultimas_corridas:
        resultados_corrida = corrida.resultados_set.all()
        resultados.extend(resultados_corrida)
    
    standings = [1,1]

  

    standings = standings[1:]
    standings = standings[(standings[:, 1]).argsort()[::-1]]


    context = {
        'standings': standings,
        'epocas' : epocas,
    }

    return HttpResponse(template.render(context, request))
    
def corridas(request):
    template = loader.get_template('brTalkingformula/corridas.html')
    items = Corrida.objects.order_by('ronda')[0:]                       #lista das corridas

    context = {
        'corridas': items,
    }
    return HttpResponse(template.render(context, request))

def corridaDetails(request, ronda):
    template = loader.get_template('brTalkingformula/corrida_detalhes.html')
    

    try:
        corrida = Corrida.objects.get(ronda = ronda)
        context = {
            'corrida' : corrida
            }
    except Corrida.DoesNotExist:
        raise Http404("Guitar does not exist")
    return HttpResponse(template.render(context, request))


def circuitos(request):
    template = loader.get_template('brTalkingformula/circuitos.html')
    items = Corrida.objects.order_by('circuitoid')[0:]
    context = {
        'circuitos':items
    }
    return HttpResponse(template.render(context, request))

def noticias(request):
  template = loader.get_template('brTalkingformula/noticias.html')
  noticias = Noticia.objects.all()
  context = {'noticias': noticias}

  return HttpResponse(template.render(context, request))

def noticiasDetails(request, noticiaid):
    template = loader.get_template('brTalkingformula/noticia_detalhes.html')
    noticia = Noticia.objects.get(noticiaid =noticiaid)

    comentarios = Comentario.objects.filter(noticia_noticiaid = noticiaid)
    novo_comentario = None

    #Quando postado um novo comentario
    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():

            # Create Comment object but don't save to database yet
            novo_comentario = comentario_form.save(commit=False)
            # Assign the current post to the comment
            novo_comentario.noticia_noticiaid = noticia.noticiaid
            # Save the comment to the database
            novo_comentario.save()
    else:
        comentario_form = ComentarioForm()

    context = {
        'noticia' : noticia,
        'comentarios': comentarios,
        'novo_comentario' : novo_comentario,
        'comentario_form' : comentario_form
               }
    return HttpResponse(template.render(context, request))
