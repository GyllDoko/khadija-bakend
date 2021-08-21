from os import name
from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "catégorie"
        verbose_name_plural = "catégories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    quantity = models.SmallIntegerField(editable=False, null=True, blank=True)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "produit"
        verbose_name_plural = "produits"

    def __str__(self):
        return self.name


class Description(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    product = models.ForeignKey(
        Product, related_name='descriptions', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "description"
        verbose_name_plural = "descriptions"

    def __str__(self):
        return self.name


def upload_image(instance, filename):
    return '/'.join(['Product Image', str(instance.product.name), filename])


class Image(models.Model):
    url = models.FileField(upload_to=upload_image, null=True, blank=True)
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"

    def __str__(self):
        return self.url.path
