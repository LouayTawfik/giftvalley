# from rest_framework import generics, authentication, permissions

from rest_framework import mixins, viewsets, generics

from .models import Address, Merchant, Store
from .serializers import AddressSerializer, MerchantSerializer, StoreSerializer





class MerchantCreateGenericView(generics.CreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = []


class MerchantListGenericView(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = []


