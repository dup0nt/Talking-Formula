from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #Pilotos
    path('pilotos', views.pilotos, name='pilotos'),
    path('pilotos/<int:pilotoid>/', views.pilotosDetails, name='pilotosDetails'),
    
    #Corridas
    path('corridas', views.corridas, name='corridas'),
    path('corrida/<int:ronda>/', views.corridaDetails, name='corridaDetails'),

    #Circuitos
    path('circuitos', views.circuitos, name='circuitos'),
    path('circuitos/<int:circuitoid>/', views.circuito, name='circuito'),


    #Noticias
    path('noticias', views.noticias, name='noticias'),
    path('noticias/<int:noticiaid>/', views.noticiasDetails, name='noticiaDetails'),


    #Resultados
    path('resultados/', views.resultados, name='resultados')

]

