from email.policy import default
from django.db import models
from merchants.models import Merchant, Store, Address
from django_extensions.db.models import TimeStampedModel




    


class Card_Design(models.Model):
    design_name = models.CharField(max_length=100, null=False)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL, null=True)
    logo = models.ImageField(null=True, upload_to='designs')





class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=11, null=False)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)



    
class Card(TimeStampedModel):
    quantity = models.IntegerField()
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    barcode = models.CharField(max_length=10, blank=True)
    expire_date = models.DateTimeField(null=True)
    is_delivered = models.BooleanField(default=False)

    
    card_design = models.ForeignKey(Card_Design, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)


    pin = models.CharField(max_length=4, blank=True)
    
 

    
    ACTIVATED = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    STATUS = [
        (ACTIVATED, 'Activated'),
        (INACTIVE, 'Inactive'),
    ]

    status = models.CharField(max_length=15, choices=STATUS, default=INACTIVE)

    activation_date = models.DateTimeField(auto_now_add=True)








class Transaction(TimeStampedModel):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    deducted_balance = models.DecimalField(max_digits=5, decimal_places=3, blank=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)












