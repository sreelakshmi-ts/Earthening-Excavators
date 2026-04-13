from django.db import models
from Shops.models import *
from Guests.models import *
# Create your models here.

class Booking(models.Model):
    booking_date=models.DateField(auto_now=True)
    excavator=models.ForeignKey(Excavator,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    booking_vsts=models.IntegerField(default=0)


class Renting(models.Model):
    quantity=models.CharField(max_length=10)
    from_date=models.DateField()
    days=models.CharField(max_length=10)
    amount=models.CharField(max_length=50)
    excavator=models.ForeignKey(Excavator,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    renting_date=models.DateField(auto_now=True)
    rent_vsts=models.IntegerField(default=0)    


class Requestoperator(models.Model):
    request=models.CharField(max_length=50)
    request_date=models.DateField(auto_now=True)
    request_vsts=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    rent=models.ForeignKey(Renting,on_delete=models.CASCADE)