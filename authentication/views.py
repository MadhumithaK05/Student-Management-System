from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from authentication.models import Stud
from authentication.models import details
from student import settings

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def students(request):
    info=Stud.objects.all()
    data= {
    "cust": info
}

    return render(request, "authentication/students.html",data)



def schedules(request):
    return render(request, "authentication/schedules.html")

def grades(request):
    return render(request, "authentication/grades.html")

def about(request):
    return render(request, "authentication/about.html")

def cal(request):
    return render(request, "authentication/cal.html")

def rule(request):
    return render(request, "authentication/rule.html")

