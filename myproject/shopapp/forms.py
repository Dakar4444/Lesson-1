from typing import Any
from django import forms


class ProductForm(forms.Form):
    image = forms.FileField(required=True,widget=forms.FileInput)
