from merchants.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

import random 
import string
from django.shortcuts import get_object_or_404

from merchants.models import Merchant

from .models import(
    Card,
    Card_Design,
    Customer,
    Transaction,
)
from .serializers import (
    CardSerializer,
    CreateCardDesginSerializer, 
    ListCardDesginSerializer,
    CreateCustomerSerializer,
    ListCustomerSerializer,
    TransactionSerializer,
    UpdateCardSerializer
)


class CardActivationAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, card_id, *args, **kwargs):
        serializer = UpdateCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        card = get_object_or_404(Card, pk=card_id)
        if card.barcode == serializer.validated_data['barcode']:
            if card.status == "ACTIVE":
                return Response(data={'pin': card.pin}, status=status.HTTP_200_OK)
            elif card.status == "INACTIVE":
                    card.pin = ''.join(random.choices(string.digits, k = 4))
                    card.status ='ACTIVE'
                    card.save()
                    return Response(data={'pin': card.pin}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CardModelViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        print(self.request)
        return qs.filter(store__merchant__id = self.request.user.id)


class CardDesignModelViewSet(viewsets.ModelViewSet):
    queryset = Card_Design.objects.all()
    serializer_class = CreateCardDesginSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(merchant_id=self.request.user.id)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(merchant_id = self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'update':
            return ListCardDesginSerializer
        else:
            return CreateCardDesginSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateCardDesginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(logo=self.request.FILES['logo'])
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'update':
            return ListCustomerSerializer
        else:
            return CreateCustomerSerializer


class TransactionModelViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(card_id= self.kwargs.get['card_id'])
