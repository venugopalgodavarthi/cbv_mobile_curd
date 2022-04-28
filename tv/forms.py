from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
class registerform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
    def save(self,commit=True):
        user=super(registerform,self).save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user