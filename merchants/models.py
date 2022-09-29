from django.db import models
from django.contrib.auth.models import User



class Governorate(models.Model):
    governorate_name = models.CharField(max_length=20)



class City(models.Model):
    city_name = models.CharField(max_length=20)
    governorate = models.ForeignKey(Governorate, on_delete=models.SET_NULL, null=True)



class Address(models.Model):
    line_1 = models.TextField(max_length=200)
    line_2 = models.TextField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)





class Merchant(User):
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=11, null=False)
    

    

class Store(models.Model):
    store_name = models.CharField(max_length=50,null=False)
    merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL, null=True, related_name='store')

    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'


    TYPE = [
        (ONLINE, 'ONLINE'),
        (OFFLINE, 'OFFLINE'),
    ]


    type = models.CharField(max_length=10, choices=TYPE, default=OFFLINE)


    address = models.OneToOneField(Address, null=True, on_delete=models.SET_NULL)
    online_store_URL = models.URLField(null=True)




    def __str__(self):
        return self.store_name
