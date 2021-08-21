from product.models import Category, Description, Image, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["name", "price", "quantity", "category", "default_image"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["url"]


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ["name", "value"]
