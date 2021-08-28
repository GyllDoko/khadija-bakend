from rest_framework import serializers
from order.models import Order, OrderProduct
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["id", "timestamp", "status",
                  "total_price", "ticket"]


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = ["id", "name", "price", "default_image", "quantity"]
