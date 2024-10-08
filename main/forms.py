from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags
import bleach

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'stock']

    def clean_name(self):
        return strip_tags(self.cleaned_data['name'])
    
    def clean_price(self):
        return strip_tags(self.cleaned_data['price'])
    
    def clean_description(self):
        return strip_tags(self.cleaned_data['description'])
    
    def clean_stock(self):
        return strip_tags(self.cleaned_data['stock'])