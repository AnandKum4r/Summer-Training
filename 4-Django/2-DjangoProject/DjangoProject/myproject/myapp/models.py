from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50,primary_key=True)

