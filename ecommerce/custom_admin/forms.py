from django import forms
from products .models import Products
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_image','product_name', 'product_price', 'stock')

class UpdateQuantityForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('stock',)      



class LoginForms(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
