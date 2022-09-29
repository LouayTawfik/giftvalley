from rest_framework import serializers
from .models import ( 
    Address,
    City,
    Governorate,
    Merchant,
    Store,
)
from django.contrib.auth.hashers import make_password


class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    governorate = GovernorateSerializer()
    class Meta:
        model = City
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Address
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    class Meta:
        model = Store
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['type'] == 'OFFLINE':
            governorate_data = validated_data['address']['city']['governorate']
            governorate = Governorate.objects.create(
                **governorate_data
            )
            
            city_data = validated_data['address']['city']
            city_data.pop('governorate')
            city = City.objects.create(
                **city_data,
                governorate=governorate
            )

            
            address_data = validated_data['address']
            address_data.pop('city')
            address = Address.objects.create(
                **address_data,
                city=city
            )
            
            validated_data.pop('address')
            store = Store.objects.create(
                **validated_data,
                address = address,
            )
        else:
            store = Store.objects.create(
                **validated_data,
            )

        return store


class MerchantSerializer(serializers.ModelSerializer):   
    address = AddressSerializer()
    store = StoreSerializer(many=True)
    class Meta:
        model = Merchant
        fields = '__all__'
        extra_kwargs = {
            'last_login': {'write_only': True}, 
            'is_superuser': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_active': {'write_only': True},
            'groups': {'write_only': True}, 
            'password': {'write_only': True, 'min_length': 8},
            'user_permissions': {'write_only': True}
        }

    def create(self, validated_data):
        governorate_data = validated_data['address']['city']['governorate']
        governorate = Governorate.objects.create(
            **governorate_data
        )

        city_data = validated_data['address']['city']
        city_data.pop('governorate')
        city = City.objects.create(
                **city_data,
                governorate=governorate
        )

        address_data = validated_data['address']
        address_data.pop('city')
        address=Address.objects.create(
            **address_data,
            city=city
        )
        
        validated_data['password'] = make_password(validated_data['password'])
        stores_data = validated_data.pop('store')
        validated_data.pop('address')
        merchant = Merchant.objects.create(
            **validated_data,
            address = address,
        )
        
        for store_data in stores_data:
            if store_data['type'] == 'OFFLINE':
                governorate_data = store_data['address']['city']['governorate']
                governorate = Governorate.objects.create(
                    **governorate_data
                )
                city_data = store_data['address']['city']
                
                city_data.pop('governorate')
                city = City.objects.create(
                    **city_data,
                    governorate=governorate
                )
                address_data = store_data['address']
                address_data.pop('city')

                address= Address.objects.create(
                    **address_data,
                    city=city
                )
                store_data.pop('address')

                Store.objects.create(
                    **store_data,
                    address = address,
                    merchant=merchant
                )
            else:
                Store.objects.create(
                    **store_data,
                    merchant=merchant
                )
        return merchant


class ListStoreSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    merchant = serializers.StringRelatedField()
    class Meta:
        model = Store
        fields = '__all__'
        extra_kwargs = {
            'last_login': {'write_only': True},
            'is_superuser': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_active': {'write_only': True},
            'groups': {'write_only': True}
        }


class UpdateStoreSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    merchant = MerchantSerializer()
    class Meta:
        model = Store
        fields = '__all__'
        extra_kwargs = {
            'last_login': {'write_only': True},
            'is_superuser': {'write_only': True},
            'is_staff': {'write_only': True},
            'is_active': {'write_only': True},
            'groups': {'write_only': True}
        }
        