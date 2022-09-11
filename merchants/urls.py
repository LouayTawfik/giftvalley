from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import MerchantCreateGenericView, MerchantListGenericView



urlpatterns = [
    # path('auth/', obtain_auth_token),
    # path('', views.MerchantGenericListView.as_view()),
    # path('', MerchantGenericView.as_view())
    path('', MerchantCreateGenericView.as_view()),
    path('list', MerchantListGenericView.as_view())
    # path('<int:pk>', views.AddressDetailView.as_view()),
]