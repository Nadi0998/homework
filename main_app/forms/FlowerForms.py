from django import forms

from main_app.models import Flower


class AddFlowerForm(forms.Form):
    @staticmethod
    def validate_price(price):
        return 0 < price <= 10000

    flower_name = forms.Field(
        label='Наименование',
        required=True
    )
    price = forms.DecimalField(
        label='Цена',
        required=True,
        validators=[validate_price]
    )
    color = forms.Field(
        label='Цвет',
        required=True,
    )
    country = forms.Field(
        label='Страна',
        required=True
    )


class SetFlowerPhotoForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['img']

    def clean_image(self):
        image = self.cleaned_data.get('img', False)
        if image:
            if image._size > 4 * 1024 * 1024:
                from django.core.exceptions import ValidationError
                raise ValidationError("Image file too large ( > 4mb )")
            return image

