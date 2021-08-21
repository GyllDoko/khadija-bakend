from order.models import Order
from django.contrib import admin

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ["ticket", "total_price", "status"]


admin.site.register(Order, OrderAdmin)
