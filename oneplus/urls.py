from django.urls import path
from oneplus import views
app_name='oneplus'
urlpatterns=[
    path('mcreate/',views.mcreate.as_view(),name="mcreate"),
    path('mselect/',views.mselect.as_view(),name="mselect"),
    path('mdetail/<int:pk>/',views.mdetail.as_view(),name="mdetail"),
    path('mupdate/<int:pk>/',views.mupdate.as_view(),name="mupdate"),
    path('mdelete/<int:pk>/',views.mdelete.as_view(),name="mdelete"),
    ]