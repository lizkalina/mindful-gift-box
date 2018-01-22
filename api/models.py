from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=50)

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    #photo =

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,blank=True)

class GiftBox(models.Model):
    items = models.ManyToManyField(Item,blank=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    giftbox = models.ManyToManyField(GiftBox,blank=True)

class CustomGiftBox(GiftBox):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
