from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def upload_avatar(instance, filename):
    return '/'.join(["Avatar", str(instance.user.last_name), str(instance.user.first_name), filename])


class Account(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Client")
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Téléphone")
    address = models.CharField(max_length=500, blank=True, null=True)
    avatar = models.FileField(upload_to=upload_avatar, blank=True, null=True)
    is_delivery_man = models.BooleanField(
        verbose_name="Livreur ?", null=True, blank=True, default=False)
    is_cook = models.BooleanField(
        verbose_name="Cuisinier ?", null=True, blank=True, default=False)

    class Meta:
        verbose_name = "compte"
        verbose_name_plural = "comptes"

    def __str__(self):
        return self.user.email
