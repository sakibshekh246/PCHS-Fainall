from django.shortcuts import render,HttpResponse, render, redirect
from django.contrib import messages
from pchs.models import User_Name
from Registration.models import Registration
from .models import Login

def index(request):
    r_data = {'data' : Registration.objects.all()}
    return render(request, './login.html',r_data)

 def login(request):
    
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                    return redirect('accounts:home')
                else:
                    request.session.set_expiry(1209600)
                    return redirect('accounts:home')
            else:
                return redirect('accounts:login')
        else:
            return redirect('accounts:registration')
    else:
        form = LoginForm()
        return render(request, "loginadmin")   



# Create your views here.
