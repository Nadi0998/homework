from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    birth_date = models.DateField(null=True)


class Flower(models.Model):
    flower_name = models.CharField(max_length=90, unique=True)
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    img = models.ImageField()


class Order(models.Model):
    order_date = models.DateField(auto_now_add=True)
    flowers = models.ManyToManyField(Flower, through='OrderDetail')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_price = models.IntegerField(null=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    flower = models.ForeignKey(Flower, models.SET_NULL, null=True)
    quantity = models.IntegerField()
