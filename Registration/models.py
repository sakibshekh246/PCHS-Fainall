from django.db import models
from pchs.models import User_Name


GENDER_CHOICES = (
   ('male', 'Male'),
   ('female', 'Female')
)

class Registration(models.Model):
    id = models.AutoField(primary_key=True)
 #user_id = models.ForeignKey('User_Name', on_delete=models.CASCADE, null=False,)
    user_name = models.CharField(max_length=200, default="0", unique=True)
    first_name = models.CharField(max_length=300, default="0")
    last_name = models.CharField(max_length=300, default="0")
    email = models.CharField(max_length=300, default="0")
    password =models.CharField(max_length=500, default="0")
    com_password = models.CharField(max_length=500, default="0")
    number = models.CharField(max_length=15, default="0")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20, default="0")
    date_of_birth = models.DateField(max_length=20, default="0")




# Create your models here.
