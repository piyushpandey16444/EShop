from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product, Category
from django.http import JsonResponse
from django.core import serializers
from .serializers import ProductSerializer, CategorySerializer
import json
from django.core.serializers.json import DjangoJSONEncoder


def home_view(request):
    if request.method == "GET":
        category_objs = Category.get_all_categories()
        get_category = request.GET.get('category_id', None)
        if get_category is not None:
            product_objs = Product.get_product_by_category(
                category_id=get_category)
        else:
            product_objs = Product.get_all_products()
        context = {
            'products': product_objs,
            'categories': category_objs,
        }
        return render(request, 'store/home.html', context)
