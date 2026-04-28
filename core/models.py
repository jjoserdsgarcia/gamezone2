from django.db import models

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
    
class Users(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username
    
class Library(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.product.name}"