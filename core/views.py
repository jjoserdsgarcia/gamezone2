from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import admin

# Create your views here.


def paginainit(request):
    return render(request, 'core/paginainit.html')
