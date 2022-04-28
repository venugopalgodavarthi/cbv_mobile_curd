from dataclasses import field
from django import forms
from oneplus.models import oneplusmodel
class oneplusform(forms.ModelForm):
    class Meta:
        model=oneplusmodel
        fields="__all__"
