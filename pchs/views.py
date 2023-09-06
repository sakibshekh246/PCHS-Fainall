from django.shortcuts import HttpResponse, render
def index(request):
    return render(request,'pchs.html')
def insert(request):
    cat_name = request.POST.get('user_name')
    Email = request.POST.get('email')
    return HttpResponse(cat_name)
