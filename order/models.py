from django.contrib.auth.models import User
from product.models import Product
from django.db import models

# Create your models here.


class Order(models.Model):

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(
        User, related_name='orders', on_delete=models.CASCADE)
    ticket = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        return self.ticket
