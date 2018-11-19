from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Flower, User, Order, OrderDetail

admin.site.register(Flower)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderDetail)