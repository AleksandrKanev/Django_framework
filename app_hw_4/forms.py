from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['info', 'price', 'quantity', 'img']
    product = forms.ModelChoiceField(queryset=Product.objects.all())
