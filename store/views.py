from django.shortcuts import render
from .models import Product


def home_view(request):
    product_objs = Product.get_all_products()
    context = {
        'products': product_objs,
    }
    return render(request, 'store/home.html', context)
