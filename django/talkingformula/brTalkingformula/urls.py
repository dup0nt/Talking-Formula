from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #Pilotos
    path('pilotos', views.pilotos, name='pilotos'),
    #path('pilotos/<int:piloto_id>/', views.pilotoDetails, name='pilotoDetails'),
    
    #Corridas
    path('corridas', views.corridas, name='corridas'),

    #Circuitos
    path('circuitos', views.circuitos, name='circuitos'),

    #Noticias
    #ultima noticia:
    path('noticias/', views.noticias, name='noticias'),

]

