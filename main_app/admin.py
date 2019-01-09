from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Flower, User, Order, OrderDetail
from .forms.UserForms import CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'birth_date', 'avatar')}),
    )


admin.site.register(Flower)
# admin.site.register(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Order)
admin.site.register(OrderDetail)