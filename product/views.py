from product.models import Category, Product
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from product.serializers import CategorySerializer, DescriptionSerializer, ImageSerializer, ProductSerializer

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.


@csrf_exempt
def get_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(data=category_serializer.data, safe=False)


@csrf_exempt
def get_products(request, category):
    if request.method == 'GET':
        category = Category.objects.get(name=category)
        products = category.products.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(data=products_serializer.data, safe=False)


@csrf_exempt
def get_images(request, product):
    if request.method == 'GET':
        product = Product.objects.get(name=product)
        images = product.images.all()
        image_serializer = ImageSerializer(images, many=True)
        return JsonResponse(data=image_serializer.data, safe=False)


@csrf_exempt
def get_descriptions(request, product):
    if request.method == 'GET':
        product = Product.objects.get(name=product)
        descriptions = product.descriptions.all()
        description_serializer = DescriptionSerializer(descriptions, many=True)
        return JsonResponse(data=description_serializer.data, safe=False)
