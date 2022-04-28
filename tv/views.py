from django.shortcuts import redirect, render
from tv.forms import registerform
from django.contrib.auth.models import User
# Create your views here.
def registerview(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/acc/login/')
    return render(request,'registration/login.html',{'form':form})