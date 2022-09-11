from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




class Address(models.Model):
    line_1 = models.TextField(max_length=100, null=False)
    line_2 = models.TextField(max_length=100, null=False)
    city = models.TextField(max_length=50, null=False)
    governorate = models.TextField(max_length=100, null=False)





class Merchant(User):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    # company = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    

    

class Store(models.Model):
    store_name = models.CharField(max_length=50,null=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    ONLINE = 'ON'
    OFFLINE = 'OFF'


    TYPE = [
        (ONLINE, 'Online'),
        (OFFLINE, 'Offline'),
    ]


    type = models.CharField(max_length=10, choices=TYPE, default=OFFLINE)


    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    online_store_URL = models.URLField(null=True)














