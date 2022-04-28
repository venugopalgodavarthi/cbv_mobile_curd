from django.urls import path
from cbv import views
urlpatterns=[
    #path('sample/',views.sample,name="sample"), #function based
    #path('csample/',views.csample.as_view(),name="csample"), #class based
    #path('psample/',views.psample.as_view(),name="psample")


    path('sample/<int:pk>/',views.sample,name="sample"), 
    path('csample/<int:pk>/',views.csample.as_view(),name="csample"),
    path('psample/<int:pk>/',views.psample.as_view(),name="psample"),
]