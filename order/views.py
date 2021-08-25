from django.shortcuts import render

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from order.serializers import Order, OrderSerializer
# Create your views here.

@csrf_exempt
def save_order(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
