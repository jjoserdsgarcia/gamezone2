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