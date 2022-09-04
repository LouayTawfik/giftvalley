from django.db import models
from merchants.models import Merchant, Address
from django_extensions.db.models import TimeStampedModel



    


class Card_Design(models.Model):
    design_name = models.CharField(max_length=100, null=False)
    logo = models.ImageField()
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)





class Customer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=11, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)



    
class Card(models.Model):
    quantity = models.IntegerField()
    balance = models.DecimalField(max_digits=5, decimal_places=3)
    barcode = models.CharField(max_length=16, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)

    
    card_design = models.ForeignKey(Card_Design, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)


    pin = models.CharField(max_length=4)
    
 

    
    ACTIVATED = 'ACTIVATE'
    INACTIVE = 'INACTIVE'

    STATUS = [
        (ACTIVATED, 'Activated'),
        (INACTIVE, 'Inactive'),
    ]

    status = models.CharField(max_length=15, choices=STATUS, default=INACTIVE)

    activation_date = models.DateTimeField(auto_now_add=True)






class Transaction(TimeStampedModel):
    name = models.CharField(max_length=100)
    transaction_balance = models.DecimalField(max_digits=5, decimal_places=3)


    card = models.ForeignKey(Card, on_delete=models.CASCADE)












