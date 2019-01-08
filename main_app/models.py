from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения')
    avatar = models.ImageField(upload_to='static/images/users', verbose_name='Аватар', blank=True)


class Flower(models.Model):
    flower_name = models.CharField(max_length=90, unique=True, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    country = models.CharField(max_length=50, verbose_name='Страна')
    img = models.ImageField(upload_to='static/images', blank=True, null=True, default='images/default.png', verbose_name='Изображение')


class Order(models.Model):
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата')
    flowers = models.ManyToManyField(Flower, through='OrderDetail', verbose_name='Цветы')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    total_price = models.IntegerField(null=True, verbose_name='Итоговая стоимость')


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    flower = models.ForeignKey(Flower, models.SET_NULL, null=True, verbose_name='Цветок')
    quantity = models.IntegerField(verbose_name='Количество')
