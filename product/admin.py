from product.models import Category, Description, Image, Product
from django.contrib import admin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "product"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["product"]
