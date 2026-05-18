from django.contrib import admin
from .models import Luminaria, Times, Volei
from .models import Library

# Register your models here.

from .models import Products, Categories, Stock, Library, Orders
admin.site.register(Products)
admin.site.register(Categories)


admin.site.register(Orders)
admin.site.register(Stock)

@admin.register(Luminaria)
class LuminariaAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'potencia', 'cor', 'preco', 'estoque', 'ativo']
    list_filter = ['cor', 'ativo']
    search_fields = ['modelo']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']

@admin.register(Volei)
class VoleiAdmin(admin.ModelAdmin):
    list_display = ['nome', 'time', 'posicao', 'jogador_ativo']
    search_fields = ['time']

@admin.register(Times)
class TimesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cidade', 'estadio']
    search_fields = ['nome']