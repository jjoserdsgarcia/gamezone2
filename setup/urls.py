"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core.views import  ProductsViewSet, TimesViewSet, VoleiViewSet, logout_view, paginacompras, paginacriarconta, paginainit, admin
from django.http import HttpResponse
from django.template import loader
from core.views import paginaloja, paginabiblioteca, paginalogin, LuminariaListView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'volei', VoleiViewSet, basename='volei')
router.register(r'times', TimesViewSet, basename='times')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('init/', paginainit, name='paginainit'),
    path('loja/', paginaloja, name='paginaloja'),
    path('biblioteca/', paginabiblioteca, name='paginabiblioteca'),
    path('login/', paginalogin, name='paginalogin'),
    path('criarconta/', paginacriarconta, name='paginacriarconta'),
    path('logout/', logout_view, name='logout'),
    path('compras/', paginacompras, name='paginacompras'),
    path('luminarias/', LuminariaListView.as_view(), name= 'luminaria_lista'),
    path('api/', include(router.urls)),
    path('api/token', obtain_auth_token, name='api_token_auth'),
]
