from django import forms
from django.forms import ModelForm
from django import forms
from .models import Product

class CreateProduct(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UploadForm(ModelForm):
    name = forms.CharField()
    seller = forms.CharField()
    price = forms.FloatField()
    dueDate = forms.DateInput()
    quantity = forms.IntegerField()
    image_url = forms.CharField()
    class Meta:
        model = Product
        fields = ['name', 'seller', 'price', 'dueDate', 'quantity', 'image_url']
