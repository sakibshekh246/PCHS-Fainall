from django.db import models
from Registration.models import Registration
from pchs.models import User_Name


class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey('Registration', on_delete=models.CASCADE, null=False,default="0")
    password =models.CharField(max_length=500, default="0")
# Create your models here.
