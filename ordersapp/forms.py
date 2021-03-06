from django import forms

from mainapp.models import Product
from ordersapp.models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', 'is_active', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='price', required=False, min_length=1, max_length=16)


    class Meta:
        model = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['product'].queryset = Product.get_items()
