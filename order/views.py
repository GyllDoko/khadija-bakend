from os import name
from order.models import OrderProduct
from django.shortcuts import render

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from order.serializers import Order, OrderProductSerializer, OrderSerializer
from product.serializers import Product
from account.models import User, Account
import random
import string
# Create your views here.


@csrf_exempt
def save_order(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user_data = data["user"]['id']
        account = Account.objects.get(pk=user_data)
        ticket = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(6))
        order = Order.objects.create(
            total_price=data["total_price"], account=account, ticket=ticket)
        for item in data["products"]:
            OrderProduct.objects.create(
                name=item["name"], price=item['price'], default_image=item['default_image'], quantity=item['quantity'], order=order)

        return JsonResponse(True, safe=False)


@csrf_exempt
def get_order(request, user):
    if request.method == "GET":
        account = Account.objects.get(pk=user)
        orders = account.orders.all()
        order_serializer = OrderSerializer(orders, many=True)
        return JsonResponse(order_serializer.data, safe=False)


@csrf_exempt
def get_order_products(request, order_id):
    if request.method == "GET":
        order = Order.objects.get(ticket=order_id)
        orders_products = order.orders_products.all()
        orders_products_serializer = OrderProductSerializer(
            orders_products, many=True)
        return JsonResponse(orders_products_serializer.data, safe=False)
