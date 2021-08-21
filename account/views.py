from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from django.contrib.auth import authenticate

from account.serializers import User, Account, UserSerializer, AccountSerializers
# Create your views here.


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_info = JSONParser().parse(request)
        username = user_info['email']
        password = user_info['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            account = Account.objects.get(user=user)
            account_serializers = AccountSerializers(account)
            data = {
                'status': True,
                'user': account_serializers.data,
            }
            return JsonResponse(data, safe=False)
        else:
            if User.objects.filter(email=username).exists():
                return JsonResponse('Veuillez entrer un mot de passe valide pour cet email !', safe=False)
            else:
                return JsonResponse(False, safe=False)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_info = JSONParser().parse(request)
        name = user_info['name']
        first_name = ""
        last_name = ""
        name_tab = name.split(' ')
        if name_tab.length > 2:
            for item in name_tab:
                if item.isupper():
                    last_name = item
                    name_tab.remove(item)
            first_name = " ".join(name_tab)
        elif name_tab == 2:
            for item in name_tab:
                if item.isupper():
                    last_name = item
                    name_tab.remove(item)
            first_name = " ".join(name_tab)
        else:
            last_name = name_tab[0]
            first_name = name_tab[name_tab.length - 1]
        print(first_name)
        print(last_name)
        username = user_info['email']
        email = user_info['email']
        password = user_info['password']
        adress = user_info['adress']
        phone_number = user_info['phone_number']
        avatar = user_info['avatar']

        if User.objects.filter(email=email).exists():
            return JsonResponse('Cet email est déja utilisé !', safe=False)

        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)
        Account.objects.create(user=user, address=adress,
                               phone_number=phone_number, avatar=avatar)
        return JsonResponse({'status': True}, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        email = data['email']
        password = data['password']
        name = data['name']
        first_name = ""
        last_name = ""
        name_tab = name.split(' ')
        if name_tab.length > 2:
            for item in name_tab:
                if item.isupper():
                    last_name = item
                    name_tab.remove(item)
            first_name = " ".join(name_tab)
        elif name_tab == 2:
            for item in name_tab:
                if item.isupper():
                    last_name = item
                    name_tab.remove(item)
            first_name = " ".join(name_tab)
        else:
            last_name = name_tab[0]
            first_name = name_tab[name_tab.length - 1]
        print(first_name)
        print(last_name)
        address = data['adress']
        phone_number = data['phone_number']
        avatar = data['avatar']
        user_id = data['id']
        user = User.objects.filter(email=email)
        for usr in user:
            first_name = first_name if first_name != "" else usr.first_name
            last_name = last_name if last_name != "" else usr.last_name
        user.update(first_name=first_name, last_name=last_name)
        account = Account.objects.filter(id=user_id)
        for acc in account:
            address = address if address != "" else acc.address
            phone_number = phone_number if phone_number != "" else acc.phone_number
            avatar = avatar if avatar != "" else acc.avatar

        account.update(address=address,
                       phone_number=phone_number, avatar=avatar)
        account = Account.objects.get(user__email=email)
        account_serializers = AccountSerializers(account)
        return JsonResponse({'status': True, 'user': account_serializers.data}, safe=False)
