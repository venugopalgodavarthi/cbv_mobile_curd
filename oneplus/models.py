from django.db import models

# Create your models here.
class oneplusmodel(models.Model):
    mseries=models.CharField(max_length=30)
    mname=models.CharField(max_length=50)
    mprice=models.IntegerField()
    mram=models.CharField(max_length=10)
    mrom=models.CharField(max_length=10)
    mpro=models.CharField(max_length=10)
    mdesc=models.CharField(max_length=100)
