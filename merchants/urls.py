from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from rest_framework import routers

from . import api



router = routers.DefaultRouter()
router.register('merchants', api.MerchantModelViewSet),
router.register('stores', api.StoreModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



