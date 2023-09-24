from django.contrib import messages
from django.shortcuts import HttpResponse, render, redirect
from .models import User_Name
def index(request):
    user_data = {'data' : User_Name.objects.all()}
    return render(request,'pchs.html',user_data)
def insert(request):
    cat_name = request.POST.get('user_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    com_password = request.POST.get('com_password')
    number = request.POST.get('number')
    data =(cat_name,email,password,com_password,number)
    
    if data:
        if len(cat_name)==0:
            messages.success(request, 'User Name Can Not Empty')
        elif '@' not in email:
            messages.success(request, 'Check email format')
        elif len(password)<6:
            messages.success(request,'The Password Minimum 6')
        elif len(com_password)<6:
            messages.success(request,'Check Password and Confum Passwoed')
        elif len(number)!=11:
             messages.success(request, 'The phone number 1 must be 11')
        elif User_Name.objects.filter(user_name=cat_name).exists():
            messages.success(request, 'This value already exists.')
        elif User_Name.objects.filter(email=email).exists():
            messages.success(request, 'This Email already exists.')    

        else:   
            user_obje = User_Name()
            user_obje.user_name = cat_name
            user_obje.email = email
            user_obje.password = password
            user_obje.com_password = com_password
            user_obje.number = number

            user_obje.save()
            messages.success(request, 'Thank You')
    else:
          messages.success(request, 'fields can not be empty')


    return redirect('useradmin')

def edit_index(request,id):
    user_obje = User_Name.objects.get(id=id)
    single_user = {'user_data':user_obje, 'id':id}
    return render(request,'edit.html',single_user)

def update(request):
    cat_name = request.POST.get('user_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    com_password = request.POST.get('com_password')
    number = request.POST.get('number')
    user_id = request.POST.get('user_id')
    data =(cat_name,email,password,com_password,number)
    
    if data:
        if len(cat_name)==0:
            messages.success(request, 'User Name Can Not Empty')
        elif '@' not in email:
            messages.success(request, 'Check email format')
        elif len(password)<6:
            messages.success(request,'The Password Minimum 6')
        elif len(com_password)<6:
            messages.success(request,'Check Password and Confum Passwoed')
        elif len(number)!=11:
             messages.success(request, 'The phone number 1 must be 11')
        elif User_Name.objects.filter(user_name=cat_name).exists():
            messages.success(request, 'This value already exists.')
        elif User_Name.objects.filter(email=email).exists():
            messages.success(request, 'This Email already exists.')    

        else:   
            user_obje = User_Name.objects.get(id=user_id)
            user_obje.user_name = cat_name
            user_obje.email = email
            user_obje.password = password
            user_obje.com_password = com_password
            user_obje.number = number

            user_obje.save()
            messages.success(request, 'Edit Successfully')
    else:
          messages.success(request, 'fields can not be empty')

    return redirect('useradmin')    

def delete(request,id):
    user_obje = User_Name.objects.get(id=id)
    user_obje.delete()
    return redirect('useradmin')     