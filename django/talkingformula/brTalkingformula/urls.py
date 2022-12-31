from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #Pilotos
    path('pilotos', views.pilotos, name='pilotos'),
    path('pilotos/<int:pilotoid>/', views.pilotosDetails, name='pilotosDetails'),
    
    #Construtores
    path('construtores', views.construtores, name='construtores'),



    #Corridas
    path('corridas', views.corridas, name='corridas'),
    path('corrida/<int:ronda>/', views.corridaDetails, name='corridaDetails'),

    #Circuitos
    path('circuitos', views.circuitos, name='circuitos'),
    path('circuitos/<int:circuitoid>/', views.circuitoDetails, name='circuitoDetails'),


    #Noticias
    path('noticias', views.noticias, name='noticias'),
    path('noticias/<int:noticiaid>/', views.noticiasDetails, name='noticiaDetails'),


    #Resultados
    path('resultados/', views.resultadosPilotos, name='resultados'),
    path('resultados/<int:epoca_ano>', views.resultadosPilotos, name='resultados'), 
]

