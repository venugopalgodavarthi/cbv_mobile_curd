from django import forms
from cbv.models import gomodel

class goform(forms.ModelForm):
    class Meta:
        model=gomodel
        fields='__all__'

