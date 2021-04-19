from django.shortcuts import render
from .models import Product, Category


def home_view(request):
    product_objs = Product.get_all_products()
    category_objs = Category.get_all_categories()
    context = {
        'products': product_objs,
        'categories': category_objs,
    }
    return render(request, 'store/home.html', context)
