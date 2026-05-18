from rest_framework import serializers

from .models import Products
from .models import Volei
from .models import Times

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'description', 'category']

class VoleiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volei
        fields = ['id', 'nome', 'time', 'posicao', 'jogador_ativo']

class TimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Times
        fields = ['id', 'nome', 'cidade', 'estadio']

