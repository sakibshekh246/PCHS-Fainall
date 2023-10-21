from django.db import models
from pchs.models import User_Name





GENDER_CHOICES = (
   ('male', 'Male'),
   ('female', 'Female')
)

class Re(models.Model):
    
    id = models.AutoField(primary_key=True)
    #user_id = models.ForeignKey('User_Name', on_delete=models.CASCADE, null=False)
    user_name = models.CharField(max_length=200,  unique=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password =models.CharField(max_length=500)
    com_password = models.CharField(max_length=500)
    number = models.CharField(max_length=15)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    date_of_birth = models.DateField(max_length=20)


   





# Create your models here.
