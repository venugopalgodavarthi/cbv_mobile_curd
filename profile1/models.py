from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class registermodel(User):
    dob=models.DateField()
    phone=models.BigIntegerField(unique=True)
    address=models.TextField()
    list1=[['Male','MALE'],['Female','FEMALE']]
    gender=models.CharField(max_length=10,choices=list1)

