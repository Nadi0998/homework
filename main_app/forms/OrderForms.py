from django import forms
from main_app.models import Flower, Order, OrderDetail


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user', '']



class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        exclude = ["order", "flower"]

    flowers = forms.ModelMultipleChoiceField(queryset=Flower.objects.all())

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['flowers'] = [t.pk for t in kwargs['instance'].flower_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)

        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()

            instance.flower_set.clear()
            instance.flower_set.add(*self.cleaned_data['toppings'])

        self.save_m2m = save_m2m

        if commit:
            instance.save()
            self.save_m2m()

        return instance
