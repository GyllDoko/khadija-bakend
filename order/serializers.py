from rest_framework import serializers
from order.models import Order
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "timestamp", "status",
                  "total_price", "product", "ticket"]
