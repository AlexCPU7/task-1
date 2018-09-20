from django import forms
from .models import Tipper, Model


class AddTipperForm(forms.ModelForm):
    class Meta:
        model = Tipper
        fields = ('number', 'model', 'weight')


class AddModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ('title', 'max_weight')
