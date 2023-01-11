from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import numpy as np



from .models import Circuito
from .models import Corrida
from .models import Piloto
from .models import Equipa
from .models import Noticia
from .models import Resultados
from .models import Epoca
from .models import ResultadoPontos
from .models import Comentario

from .forms import ComentarioForm

from .standings import calc_resultadosPilotos
# Create your views here.

def index(request):
    template = loader.get_template('brTalkingformula/index.html')
    
    ultima_noticia = Noticia.objects.latest('criadoem')
    standings = calc_resultadosPilotos()
    ultima_corrida = Corrida.objects.latest('ocorreem')
    ultimo_resultados = Resultados.objects.filter(corrida_ronda = ultima_corrida.ronda)[:3]
    
    context = {
        'noticia': ultima_noticia,
        'ultima_corrida': ultima_corrida,
        'ultimo_resultado': ultimo_resultados,
        'standings' : standings,
    }
    return HttpResponse(template.render(context, request))

def pilotos(request):
    template = loader.get_template('brTalkingformula/pilotos.html')
    items = Piloto.objects.order_by('nome')[0:]
    context = {
        'pilotos':items
    }

    return HttpResponse(template.render(context, request))


def circuitoDetails(request, circuitoid):
    template = loader.get_template('brTalkingformula/circuito.html')
    
    try:
        items = Circuito.objects.get(circuitoid = circuitoid)    
        
    except Circuito.DoesNotExist:
        raise Http404("Circuito does not exist")


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
        raise Http404("Piloto does not exist")
    return HttpResponse(template.render(context, request))
    


def resultadosPilotos(request, epoca_ano=Epoca.objects.first().ano): 
    template = loader.get_template('brTalkingformula/resultados.html')
    epocas = Epoca.objects.all()
    standings = calc_resultadosPilotos(epoca_ano)

    context = {
        'standings': standings,
        'epocas' : epocas,
    }
    
    return HttpResponse(template.render(context, request))

def construtores(request):
    template = loader.get_template('brTalkingformula/construtores.html')
    #construtores = Construtor.objects.all()
    equipa = Equipa.objects.all()
    context = {
        'equipas' : equipa
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
        pontos = ResultadoPontos.objects.all()
        resultado = []
        try: 
            resultado = Resultados.objects.filter(corrida_ronda = ronda)
            
        except Resultados.DoesNotExist:
            raise Http404("Resultado não existe")
        
        context = {
            'corrida' : corrida,
            'resultado': resultado,
            'pontos' : pontos
            }
    except Corrida.DoesNotExist:
        raise Http404("Corrida does not exist")
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

            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.noticia_noticiaid = noticia
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