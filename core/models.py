from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     def __str__(self):
#         return self.username
    
class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.product.name}"
    
class Stock(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.product.name} - {self.quantity} Em estoque"
    

class Luminaria(models.Model):
    modelo = models.CharField(max_length=100)
    potencia = models.IntegerField()
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['modelo']
    
    def __str__(self):
        return self.modelo
    
class Times(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)

    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome    
    
class Volei(models.Model):
    nome = models.CharField(max_length=100)
    time = models.ForeignKey(Times, on_delete=models.CASCADE)
    posicao = models.CharField(max_length=50)
    jogador_ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
