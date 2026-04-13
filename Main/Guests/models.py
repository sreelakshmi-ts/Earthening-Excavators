from django.db import models
from Admin.models import *

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    place=models.ForeignKey("Admin.Place",on_delete=models.CASCADE)
    photo=models.FileField(upload_to='userphoto/')
    proof=models.FileField(upload_to='userproof/')
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Shop(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    place=models.ForeignKey("Admin.Place",on_delete=models.CASCADE)
    photo=models.FileField(upload_to='shopphoto/')
    proof=models.FileField(upload_to='shopproof/')
    password=models.CharField(max_length=10)
    shop_vsts=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


