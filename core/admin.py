from django.contrib import admin

# Register your models here.

from .models import Products, Categories, Stock, Library, Orders
admin.site.register(Products)
admin.site.register(Categories)

admin.site.register(Library)
admin.site.register(Orders)
admin.site.register(Stock)