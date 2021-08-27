from os import name
from order.models import OrderProduct
from django.shortcuts import render

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from order.serializers import Order, OrderSerializer
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
