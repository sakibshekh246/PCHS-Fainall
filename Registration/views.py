from django.shortcuts import render,HttpResponse, render, redirect
from django.contrib import messages
from pchs.models import User_Name
from .models import Re
# Create your views here.
def index(request):
    user_data = {'data' : User_Name.objects.all()}
    return render(request, './registration.html',user_data)


def insert(request):
    cat_name = request.POST.get('user_name')
    first_name = request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    com_password = request.POST.get('com_password')
    number = request.POST.get('number')
    gender = request.POST.get('gender')
    context = {
        'gender': gender,
    }
    date_of_birth = request.POST.get('date_of_birth')
    r_data = (cat_name,first_name,last_name,email,password,com_password,number,gender,date_of_birth)

    if r_data:
        if len(cat_name)==0:
            messages.success(request, 'User Name Can Not Empty')
        elif len(first_name)<3:
            messages.success(request,'Please Write Your First')
        elif len(last_name)<2:
            messages.success(request,'Write Your Last Name')    
        elif '@' not in email:
            messages.success(request, 'Check email format')
        elif len(password)<6:
            messages.success(request,'The Password Minimum 6')
        elif len(com_password)<6:
            messages.success(request,'Check Password and Confum Passwoed')
        elif len(number)!=11:
             messages.success(request, 'The phone number 1 must be 11')
        elif gender not in ['Male', 'Female']:
            messages.error(request, 'Invalid gender selection')
        elif not(date_of_birth): 
            messages.error(request, 'Invalid date of birth format or value')
        elif Re.objects.filter(username=cat_name).exists():
                messages.error(request, 'This username already exists.')
        elif Re.objects.filter(email=email).exists():
                messages.error(request, 'This Email already exists.')    
        else:
            regis_obje = Re()
            regis_obje.user_name = cat_name
            regis_obje.first_name = first_name
            regis_obje.last_name = last_name
            regis_obje.email = email
            regis_obje.password = password
            regis_obje.com_password = com_password
            regis_obje.number = number
            regis_obje.gender = gender
            regis_obje.date_of_birth = date_of_birth
            regis_obje.save()
            messages.success(request, 'Thank You for Registering')
    else:
          messages.success(request, 'Fields can not be empty')        

    return redirect('registrationadmin')

    