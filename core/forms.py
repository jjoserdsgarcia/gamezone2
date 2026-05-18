from django import forms
from .models import Luminaria

class LuminariaForm(forms.Form):
    class Meta:
        model: Luminaria
        fields = ['modelo', 'potencia', 'cor', 'preco', 'estoque', 'ativo']

        labels = {
            'modelo': 'Modelo',
            'potencia': 'Potencia',
            'cor': 'Cor',
            'preco': 'Preco',
            'estoque': 'Estoque',
            'ativo': 'Ativo'
        }

        widgets = {}


from .models import Library
class LibraryForm(forms.Form):
    class Meta:
        model: Library
        fields = ['user', 'product']
        labels = {
            'user': 'Usuário:',
            'product': 'Produto:'
        }
        widgets = {}


from .models import Volei
class VoleiForm(forms.Form):
    class Meta:
        model: Volei
        fields = ['nome', 'time', 'posicao', 'jogador_ativo']
        labels = {
            'nome': 'Nome:',
            'time': 'Time:',
            'posicao': 'Posição:',
            'jogador_ativo': 'Jogador Ativo:'
        }
        widgets = {}

from .models import Times
class TimesForm(forms.Form):
    class Meta:
        model: Times
        fields = ['nome', 'cidade', 'estadio']
        labels = {
            'nome': 'Nome:',
            'cidade': 'Cidade:',
            'estadio': 'Estádio:'
        }
        widgets = {}