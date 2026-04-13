from django.db import models
from Guests.models import *
# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    
class District(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Place(models.Model):
    name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Shoptype(models.Model):
    shoptype=models.CharField(max_length=50)

    def __str__(self):
        return self.shoptype

class Complainttype(models.Model):
    complaintyp=models.CharField(max_length=50)

    def __str__(self):
        return self.complaintyp

class Brandtype(models.Model):
    brandtype=models.CharField(max_length=50)
    def __str__(self):
        return self.brandtype


class Complaint(models.Model):
    complainttype=models.ForeignKey(Complainttype,on_delete=models.CASCADE)
    complaint_details=models.CharField(max_length=100)
    complaint_date=models.DateField(auto_now=True)
    complaint_vsts=models.IntegerField(default=0)
    complaint_replay=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    shop=models.ForeignKey(Shop,on_delete=models.SET_NULL,null=True)

class Feedback(models.Model):
    feedback_details=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    shop=models.ForeignKey(Shop,on_delete=models.SET_NULL,null=True)


