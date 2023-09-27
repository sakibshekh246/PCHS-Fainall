from django.shortcuts import render,HttpResponse
from pchs.models import User_Name
# Create your views here.
def index(request):
    user_data = {'data' : User_Name.objects.all()}
    return render(request, './registration.html',user_data)


