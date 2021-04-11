from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'description',
                    'create_date', 'write_date')
    list_display_links = ('id', 'name', 'category', 'price', 'description',
                          'create_date', 'write_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_date', 'write_date')
    list_display_links = ('id', 'name', 'create_date', 'write_date')
