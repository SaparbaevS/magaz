from django import forms

from app.models import Magazin


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Magazin
        fields = ['title', 'category', 'price', 'status']