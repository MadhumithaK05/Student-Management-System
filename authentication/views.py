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

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        ch1=Stud.objects.filter(sid=username)
        pwd=ch1[0]
        #messages.success(request, "Value= {%d} ".format(pwd))
        if password==pwd:
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Bad Credentials")
            return redirect("signin")
        
    return render(request, "authentication/signin.html")

def students(request):
    info=Stud.objects.all()
    data= {
    "cust": info
}

    return render(request, "authentication/students.html",data)

def signup(request):
    if request.method == "POST":
        
        rno=request.POST['rno']
        username = request.POST['username']
        email = request.POST['email']
        phone= request.POST['phone']
        fname=request.POST['fname']
        mname=request.POST['mname']
        password = request.POST['password']
        #conpwd = request.POST['conpwd']
        
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()
        
        myuser1 = details(rno=rno, username=username, email=email, fname=fname, mname=mname, password=password)
        myuser1.phone=int(phone)
        myuser1.save()
        
        messages.success(request, "Successfully Registered")
        return redirect('signin')
        
    return render(request ,"authentication/signup.html")
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

def signout(request):
    logout(request)
    messages.success(request,"Loged out Successfully")
    return redirect('home')