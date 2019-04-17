from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ('title','price', 'image')
    list_display = ('title','price', 'image')
    
admin.site.register(Product, ProductAdmin)