from django.shortcuts import render,HttpResponse, render, redirect
from django.contrib import messages
from pchs.models import User_Name
from Registration.models import Registration
from .models import Login

def index(request):
    r_data = {'data' : Registration.objects.all()}
    return render(request, './login.html',r_data)

    

# Create your views here.
