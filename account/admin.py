from account.models import Account
from django.contrib import admin

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', "is_delivery_man", "is_cook"]


admin.site.register(Account, AccountAdmin)
