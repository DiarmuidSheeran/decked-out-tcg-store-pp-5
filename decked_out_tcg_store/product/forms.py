from django import forms
from django.utils.text import slugify
from .models import Product

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        def save(self, commit=True):
            instance = super(CreateProductForm, self).save(commit=False)
            
            instance.slug = slugify(instance.name)

            if commit:
                instance.save()
            return instance

