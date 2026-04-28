from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import admin

# Create your views here.


def paginainit(request):
    return render(request, 'core/paginainit.html')

def paginaloja(request):
    from .models import Products
    products = Products.objects.all()
    return render(request, 'core/paginaloja.html', {'products': products})

def paginabiblioteca(request):
    from .models import Library
    library = Library.objects.all()
    return render(request, 'core/paginabiblioteca.html', {'library': library})