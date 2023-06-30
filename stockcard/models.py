from doctest import OutputChecker
from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.



class Customers(models.Model):
    id=models.IntegerField(blank=False, primary_key=True)
    name=models.CharField(max_length=100)
    phone_no_1=models.BigIntegerField( blank=False)
    phone_no_2=models.BigIntegerField( blank=False)
    reg_date=models.DateTimeField( blank=False)
    mail=models.EmailField(blank=True)
    address=models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(str(self.id) + " - "+self.name)

class items(models.Model):
    name=models.CharField(max_length=100, blank=False, primary_key=True)
    price=models.FloatField()
    available=models.BooleanField()
    inventory=models.IntegerField()

    def __str__(self) -> str:
        return str(self.name)


class Stock_card(models.Model):
    c_id=models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_id=models.IntegerField(blank=False, primary_key=True)
    date=models.DateTimeField( blank=False)
    item=models.ForeignKey(items, on_delete=models.DO_NOTHING)
    order=models.IntegerField(blank=False)
    amount=models.FloatField(blank=False)
    advance=models.FloatField(blank=True, null=True)
    balance=models.FloatField()
    outstanding=models.FloatField(null=True,blank=False)
    total_p=models.FloatField(null=True)
    means_of_Pay=models.CharField(max_length=100, blank=False)

    def __str__(self) -> str:
        return str(self.order_id)

class C_stat(models.Model):
    customer=models.OneToOneField(Customers, on_delete=models.CASCADE)
    advance=models.FloatField(blank=True, null=True, default=0.0)
    out=models.FloatField(null=True,blank=False,default=0.0)
    paid=models.FloatField(null=True,blank=False,default=0.0)
    def __str__(self) -> str:
        return str(self.customer.id)
