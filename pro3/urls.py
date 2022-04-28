"""pro3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pro3 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/',include('django.contrib.auth.urls')),
    path('home/',views.home,name="home"),
    path('tv/',include('tv.urls')),
    path('p/',include('profile1.urls')),
    path('c/',include('cbv.urls')),
    path('o/',include('oneplus.urls')),
]
