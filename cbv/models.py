from django.db import models

# Create your models here.
class gomodel(models.Model):
    name=models.CharField(max_length=23)
    age=models.IntegerField()
    