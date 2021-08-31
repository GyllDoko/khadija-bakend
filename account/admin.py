from account.models import Account
from django.contrib import admin
from django.contrib.auth.models import User, Group

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', "is_delivery_man", "is_cook"]


admin.site.register(Account, AccountAdmin)
# admin.site.unregister(User)
admin.site.unregister(Group)
# default: "Django Administration"
admin.site.site_header = 'Restaurant App Administration'
# default: "Site administration"
admin.site.index_title = 'Restaurant'
admin.site.site_title = 'Restaurant App | Admin'
admin.site.enable_nav_sidebar = False
