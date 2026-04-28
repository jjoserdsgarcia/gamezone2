from django.contrib import admin

# Register your models here.

from .models import Products, Categories, Users, Library, Orders
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Users)
admin.site.register(Library)
admin.site.register(Orders)