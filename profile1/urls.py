from django.urls import path
from profile1 import views
app_name='profile1'
urlpatterns=[
    path('register/',views.registerview, name="register"),
    path('login/',views.loginview, name="login"),
    path('logout/',views.logoutview, name="logout"),
    path('home/',views.homeview, name="home"),
    ]