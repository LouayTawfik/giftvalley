from rest_framework import serializers
from .models import Card, Card_Design, Customer, Transaction
from merchants.serializers import (
    AddressSerializer,
    Governorate,
    City,
    Address,
    ListStoreSerializer,
)

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

import string
import random 


class CreateCardDesginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_Design
        fields = '__all__'

    def create(self, validated_data):
        print(self.context['request'].user.id )
        print(validated_data['store'].merchant.id)
        if self.context['request'].user.id != validated_data['store'].merchant.id:
            raise ValidationError('Not Authorized')
        return super().create(validated_data)


class CreateCustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

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
        address = Address.objects.create(
            **address_data,
            city=city
        )

        validated_data.pop('address')
        customer_data = validated_data

        customer = Customer.objects.create(
            **customer_data,
            address=address
            
        )
        return customer


class ListCustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Customer
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def create(self, validated_data):
        print(self.context['request'].user.id )
        print(validated_data['store'].merchant.id)
        if self.context['request'].user.id != validated_data['store'].merchant.id:
            raise ValidationError('Not Authorized')

        card = Card.objects.create(
            quantity = validated_data['quantity'],
            balance = validated_data.get('balance'), 
            barcode = ''.join(random.choices(string.ascii_letters + string.digits, k = 10)),
            expire_date = validated_data.get('expire_date'),
            is_delivered = validated_data['is_delivered'],
            pin = "",
            status = validated_data['status'],
            card_design=validated_data['card_design'],
            store=validated_data['store'],
            customer = validated_data.get('customer'),
        )
        return card
    

class UpdateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ListCardDesginSerializer(serializers.ModelSerializer):
    store = ListStoreSerializer()
    card = CardSerializer(source='card_set', many=True)
    class Meta:
        model = Card_Design
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs={
            'deducted_balance': {'required': True},
            'card': {'read_only': True}        
        }

    def create(self, validated_data):
        cardId = self.context['request'].parser_context['kwargs']['card_id']
        card = get_object_or_404(Card, pk=cardId)
        if card.balance != None:
            if validated_data['deducted_balance'] <= card.balance:
                card.balance -= validated_data['deducted_balance'] 
                card.save()
            else:
                raise ValidationError('Sorry, the deducted amount from balance is greater than the card balance')
        validated_data['card'] = card
        return super().create(validated_data)
