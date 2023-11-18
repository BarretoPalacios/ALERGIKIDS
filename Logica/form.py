from django import forms
from.views import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['autor','comentario']
       