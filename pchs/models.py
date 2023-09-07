from django.db import models
class User_Name(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    password =models.CharField(max_length=500)
    com_password = models.CharField(max_length=500)
    number = models.CharField(max_length=15)
     

