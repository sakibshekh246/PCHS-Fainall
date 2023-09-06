from django.shortcuts import HttpResponse, render
def index(request):
    return render(request,'pchs.html')
def insert(request):
    cat_name = request.POST.get('user_name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = request.POST.get('com_password')
    number = request.POST.get('number')
    
    return HttpResponse(cat_name)
