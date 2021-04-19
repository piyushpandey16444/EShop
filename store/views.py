from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product, Category
from django.http import JsonResponse
from django.core import serializers
from .serializers import ProductSerializer, CategorySerializer
import json
from django.core.serializers.json import DjangoJSONEncoder


def home_view(request):
    if request.method == "GET" and request.is_ajax():
        json_category_id = request.GET.get("category_id", None)
        if json_category_id is not None:
            req_obj = Product.objects.filter(
                category=json_category_id).values()
            product_objs = json.dumps(list(req_obj), cls=DjangoJSONEncoder)
            return JsonResponse(data=product_objs, safe=False)
    else:
        product_objs = Product.get_all_products()
        category_objs = Category.get_all_categories()
        context = {
            'products': product_objs,
            'categories': category_objs,
        }
        return render(request, 'store/home.html', context)
