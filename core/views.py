from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Products, Categories, Stock, Library, Orders
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

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
