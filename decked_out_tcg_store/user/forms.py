from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
   
    fname = forms.CharField(max_length=200, required=True)
    lname = forms.CharField(max_length=200, required=True)
    shipping_address_line_1 = forms.CharField(max_length=200, required=True)
    shipping_address_line_2 = forms.CharField(max_length=200, required=False)
    shipping_address_town = forms.CharField(max_length=200, required=True)
    shipping_address_county = forms.CharField(max_length=200, required=True)
    shipping_address_eircode =forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'fname',
            'lname',
            'shipping_address_line_1',
            'shipping_address_line_2',
            'shipping_address_town',
            'shipping_address_county',
            'shipping_address_eircode',
        ]