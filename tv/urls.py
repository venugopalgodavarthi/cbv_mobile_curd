from django.urls import path
from tv import views
urlpatterns=[
    path('register/',views.registerview,name="register"),
    ]