from django.contrib import admin

# Register your models here.
from .models import Circuito
from .models import Corrida
from .models import Piloto
from .models import PilotoEquipa
from .models import Equipa
from .models import Construtor
from .models import Resultados

admin.site.register(Circuito)
admin.site.register(Corrida)
admin.site.register(Piloto)
admin.site.register(PilotoEquipa)
admin.site.register(Equipa)
admin.site.register(Construtor)
admin.site.register(Resultados)