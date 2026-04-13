from django.db import models
from Admin.models import *
from Guests.models import *
from Users.models import *

# Create your models here.
class Operator(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='Operatorphoto/')
    proof=models.FileField(upload_to='Operatorproof/')
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Excavator(models.Model):
    name=models.CharField(max_length=50)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brandtype=models.ForeignKey(Brandtype,on_delete=models.SET_NULL,null=True)
    details=models.CharField(max_length=100)
    price=models.CharField(max_length=50,null=True)
    shoptype=models.ForeignKey(Shoptype,on_delete=models.CASCADE)
    image=models.FileField(upload_to='Excavatorsphoto/')
    shop=models.ForeignKey(Shop,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class AssignOperator(models.Model):
    operator=models.ForeignKey(Operator,on_delete=models.CASCADE)
    request=models.ForeignKey("Users.Requestoperator",on_delete=models.CASCADE)
    assign_vsts=models.IntegerField(default=0)


class Gallery(models.Model):
    image=models.FileField(upload_to='ExcavatorsGallery/')
    excavator=models.ForeignKey(Excavator,on_delete=models.CASCADE)


