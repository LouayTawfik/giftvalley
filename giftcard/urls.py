from django.urls import path, include

from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register('giftcards', api.CardModelViewSet)
router.register('cardDesign', api.CardDesignModelViewSet)
router.register('customers', api.CustomerModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('giftcards/<int:card_id>/activate/', api.CardActivationAPIView.as_view()),
    path('giftcards/<int:card_id>/tranactions/', api.TransactionModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('giftcards/<int:card_id>/tranactions/<int:pk>/', api.TransactionModelViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
]

