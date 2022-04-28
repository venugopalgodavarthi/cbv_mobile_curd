from django.shortcuts import redirect, render

def home(request):
    return render(request,'welcome.html')

def logout(request):
    return redirect('acc/logout/')
