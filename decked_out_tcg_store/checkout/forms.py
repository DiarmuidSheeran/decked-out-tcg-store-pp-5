from django import forms

class CheckoutForm(forms.Form):
    shipping_address_line_1 = forms.CharField(max_length=100)
    shipping_address_line_2 = forms.CharField(max_length=100, required=False)
    shipping_address_town = forms.CharField(max_length=50)
    shipping_address_county = forms.CharField(max_length=50)
    shipping_address_eircode = forms.CharField(max_length=10)
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    email = forms.EmailField()