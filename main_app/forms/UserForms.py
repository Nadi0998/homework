from django import forms
from django.contrib.auth.forms import UserChangeForm
from django_registration.forms import RegistrationForm

from main_app.models import User, Flower, Order


class CustomUserRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'avatar']

    def clean_image(self):
        image = self.cleaned_data.get('avatar_file', False)
        if image:
            if image._size > 4 * 1024 * 1024:
                from django.core.exceptions import ValidationError
                raise ValidationError("Image file too large ( > 4mb )")
            return image

