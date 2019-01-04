from django import forms
from django.contrib.auth.forms import UserChangeForm
from django_registration.forms import RegistrationForm

from main_app.models import User


class CustomUserRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email']
