import numpy as np
from django.db.models import Sum
from django.db.models import Q



from .models import PilotoEquipa
from .models import Resultados
from .models import Epoca


def calc_resultadosPilotos(epoca_ano=Epoca.objects.first().ano):

    standings = np.empty((0, 2), dtype=object)
    only_standings = np.empty(0, dtype=int)


    for pilotoEquipa in (PilotoEquipa.objects.filter(Q(equipa_equipaid__epoca_ano__ano=epoca_ano))):

        # Calculate the sum of the posfinal.pontos values for this piloto_pilotoid
        total_pontos = Resultados.objects.filter(piloto_pilotoid=pilotoEquipa.piloto_pilotoid).aggregate(Sum('posfinal__pontos'))['posfinal__pontos__sum']

        # Add the piloto_pilotoid and total_pontos values to the NumPy array
        standings = np.vstack([standings, [pilotoEquipa, total_pontos]]) 
        only_standings = np.append(only_standings, total_pontos)

    #como o standings é um mix de tipos de dados irei

    sorted_indices = np.argsort(only_standings)[::-1]
    standings = standings[sorted_indices]

    
    return standings