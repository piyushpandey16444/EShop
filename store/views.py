from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Product, Category
from django.http import JsonResponse
from django.core import serializers
from .serializers import ProductSerializer, CategorySerializer


def home_view(request):
    if request.method == "GET" and request.is_ajax():
        json_obj = request.GET.get("category_id", None)
        if json_obj is not None:
            product_objs = get_list_or_404(Product, category=json_obj)
            print("product_objs: ", product_objs)
            serializer = ProductSerializer(product_objs)
            print("serializer : ", serializer.data)
            return JsonResponse(data=serializer.data, safe=False)
    else:
        product_objs = Product.get_all_products()
        category_objs = Category.get_all_categories()
        context = {
            'products': product_objs,
            'categories': category_objs,
        }
        return render(request, 'store/home.html', context)
