from django.db import models
from Registration.models import Registration
from login.models import Login
class User_Name(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200, default="0", unique=True)
    email = models.CharField(max_length=300, default="0")
    password =models.CharField(max_length=500, default="0")
    com_password = models.CharField(max_length=500, default="0")
    number = models.CharField(max_length=15, default="0")
     

