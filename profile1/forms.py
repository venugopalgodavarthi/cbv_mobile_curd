from django import forms
from profile1.models import registermodel
from django.contrib.auth.hashers import make_password

class registerform(forms.ModelForm):
    class Meta:
        model=registermodel
        fields=['first_name','last_name','username','email','dob','gender','address','phone','password']
        widgets={'password':forms.PasswordInput,'address':forms.Textarea(attrs={'rows':3})}
    repassword=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        pas=self.cleaned_data['password']
        rpas=self.cleaned_data['repassword']
        if not(pas==rpas):
            raise forms.ValidationError('password and repassword should be same')

    def save(self,commit=True):
            user=super(registerform,self).save(commit=False)
            user.password=make_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user


class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


        