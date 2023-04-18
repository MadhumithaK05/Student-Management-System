from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from authentication.models import Stud
#from authentication.models import attend
from student import settings

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def adminlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        if username=="admin" and password=="rec":
            return render(request, "authentication/custom.html")
        else:
            messages.error(request, "Bad Credentials")
            return redirect("adminlogin")
        
    return render(request, "authentication/adminlogin.html")

def students(request):
    info=Stud.objects.all()
    data= {
    "cust": info
}

    return render(request, "authentication/students.html",data)

def schedules(request):
    return render(request, "authentication/schedules.html")

def signout(request):
    logout(request)
    messages.success(request,"Loged out Successfully")
    return redirect('home')