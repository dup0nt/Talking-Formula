from django.contrib import admin

# Register your models here.
from .models import Circuito
from .models import Corrida
from .models import Piloto
from .models import PilotoEquipa
from .models import Equipa
from .models import Construtor
from .models import Resultados
from .models import Comentario
from .models import Epoca
from .models import Noticia

admin.site.register(Circuito)
admin.site.register(Corrida)
admin.site.register(Piloto)
admin.site.register(PilotoEquipa)
admin.site.register(Equipa)
admin.site.register(Construtor)
admin.site.register(Resultados)
admin.site.register(Comentario)
admin.site.register(Epoca)
admin.site.register(Noticia)

