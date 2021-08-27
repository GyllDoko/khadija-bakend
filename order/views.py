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
        idsTab = []
        for item in data["products"]:
            idsTab.append(item["id"])
        products = Product.objects.filter(pk__in=idsTab)
        user_data = data["user"]['id']
        account = Account.objects.get(pk=user_data)
        ticket = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(6))
        order = Order.objects.create(
            total_price=data["total_price"], account=account, ticket=ticket)
        for product in products:
            order.product.add(product)
        order.save()

        return JsonResponse(True, safe=False)
