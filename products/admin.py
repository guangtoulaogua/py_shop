from django.contrib import admin
from .models import Product


class ProdutAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')






admin.site.register(Product, ProdutAdmin)

# Register your models here.
