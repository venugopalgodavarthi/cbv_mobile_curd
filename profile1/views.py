from django.shortcuts import render,redirect
from profile1.models import registermodel
from profile1.forms import registerform,loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerview(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/acc/login')
    return render(request,'registration/login.html',{'form':form})

def loginview(request):
    form=loginform()
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                print(user.id)
                login(request,user)
                return redirect('/p/home/')
    return render(request,'registration/login.html',{'form':form})

def logoutview(request):
    logout(request)
    return redirect('/p/login')

@login_required(login_url='/p/login/')
def homeview(request):
    return render(request,'home.html')

