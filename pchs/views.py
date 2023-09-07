from pyexpat.errors import messages
from django.shortcuts import HttpResponse, render, redirect
from .models import User_Name
def index(request):
    return render(request,'pchs.html')
def insert(request):
    cat_name = request.POST.get('user_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    com_password = request.POST.get('com_password')
    number = request.POST.get('number')
    
    user_obje = User_Name()
    user_obje.user_name = cat_name
    user_obje.email = email
    user_obje.password = password
    user_obje.com_password = com_password
    user_obje.number = number
    user_obje.save()
    messages.succes(request, 'Thank You')
    return redirect('useradmin')


