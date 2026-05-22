from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from core.serializers import  ProductsSerializer, VoleiSerializer, TimesSerializer
from .models import Products, Categories, Stock, Library, Orders, Luminaria, Volei, Times
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

# Create your views here.


def paginainit(request):
    return render(request, 'core/paginainit.html')

def paginaloja(request):
    messages.info(request, 'Bem-vindo à nossa loja digital.')
    messages.warning(request, 'calma ai mano')
    messages.error(request, 'god lil bro errou tudo')
    from .models import Products
    products = Products.objects.all()
    return render(request, 'core/paginaloja.html', {'products': products})

def paginabiblioteca(request):
    from .models import Library
    library = Library.objects.all()
    print (library)
    return render(request, 'core/paginabiblioteca.html', {'library': library})

def paginalogin(request):
    if request.method == 'GET':
        return render(request, 'core/paginalogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('paginainit')
        else:
            return render(request, 'core/paginalogin.html', {'error': 'Credenciais inválidas'})

def paginacriarconta(request):
    if request.method == 'GET':
        return render(request, 'core/paginacriarconta.html')
    elif request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        user = User(username=username, email=email, password=password)
        user.save()
        return redirect('paginalogin')
    
def logout_view(request):
    logout(request)
    return redirect('paginainit')

def paginacompras(request):
    from .models import Orders
    orders = Orders.objects.filter(user=request.user)
    return render(request, 'core/paginacompras.html', {'orders': orders})


class LuminariaListView(ListView):
    model = Luminaria
    template_name = 'core/luminaria/lista.html'
    context_object_name = 'luminarias'

class LibraryListView(ListView):
    model = Library
    template_name = 'core/librari/library.html'

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]


class VoleiViewSet(viewsets.ModelViewSet):
    queryset = Volei.objects.all()
    serializer_class = VoleiSerializer
    permission_classes = [IsAuthenticated]

class TimesViewSet(viewsets.ModelViewSet):
    queryset = Times.objects.all()
    serializer_class = TimesSerializer
    permission_classes = [IsAuthenticated]