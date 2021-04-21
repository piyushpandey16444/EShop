from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product, Category
from django.http import JsonResponse
from django.core import serializers
from .serializers import ProductSerializer, CategorySerializer
import json
from django.core.serializers.json import DjangoJSONEncoder


def compute_order(get_category=None, get_filter=None):
    if get_filter == 'l2h':
        product_objs = Product.get_product_by_category(
            category_name=get_category).order_by('price')
    else:
        product_objs = Product.get_product_by_category(
            category_name=get_category).order_by('-price')
    return product_objs


def home_view(request):
    if request.method == "GET" and request.is_ajax():
        get_category = request.GET.get('category_name', None)
        get_filter = request.GET.get('get_filter', None)
        product_objs = compute_order(
            get_category=get_category, get_filter=get_filter)
        return JsonResponse(data={'response': list(product_objs.values())}, safe=False)

    elif request.method == "GET":
        category_objs = Category.get_all_categories()

        get_category = request.GET.get('category_name', None)
        get_price = request.GET.get('price', None)
        if get_category is not None:
            product_objs = Product.get_product_by_category(
                category_name=get_category)
        elif get_price is not None:
            if get_price == 'l2h':
                product_objs = Product.get_product_by_category(
                    category_name=None).order_by('price')
            else:
                product_objs = Product.get_product_by_category(
                    category_name=None).order_by('-price')
        else:
            product_objs = Product.get_product_by_category(
                category_name=None)

        context = {
            'products': product_objs,
            'categories': category_objs,
        }
        return render(request, 'store/home.html', context)
