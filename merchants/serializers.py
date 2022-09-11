from rest_framework import serializers

from .models import Address, Merchant, Store
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']





class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'line_1',
            'line_2',
            'city',
            'governorate',
        ]



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


        
        


class MerchantSerializer(serializers.ModelSerializer):   
    address = AddressSerializer()
    store = StoreSerializer()

    class Meta:
        model = Merchant
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'username',
            'address',
            'store',
            'phone_number',
        ]
        extra_kwargs = {'first_name': {'required': True}, 'last_name': {'required': True}, 'email': {'required': True}, 'password': {'required': True}, 'username': {'required': True}}


    def create(self, validated_data):
        address_data = validated_data['address']
        store_data  = validated_data['store']

        address = Address.objects.create(
            line_1 = address_data['line_1'],
            line_2 = address_data['line_2'],
            city = address_data['city'],
            governorate = address_data['governorate']
        )

        store = Store.objects.create(
            store_name = store_data['store_name'],
            type = store_data['type']
            
        )

        validated_data['store'] = store
        validated_data['address'] = address
        validated_data['password'] = make_password(validated_data['password'])
        instance = super().create(validated_data)
        return instance




        