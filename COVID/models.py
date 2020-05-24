from django.db import models

# Create your models here.
class User(models.Model):
    username=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class Cart(models.Model):
    name = models.CharField(max_length=20,default='None')
    category = models.CharField(max_length=20,default='None')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default = 0)
class Item(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField(default = 0)

