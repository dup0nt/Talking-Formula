from .models import Comentario
from .models import Noticia
from django import forms

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nome', 'corpo')

