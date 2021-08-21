
from rest_framework import serializers
from account.models import User, Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'last_name', 'email']


class AccountSerializers(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ['id', 'user', 'phone_number', 'address',
                  'avatar', 'is_delivery_man', 'is_cook']
