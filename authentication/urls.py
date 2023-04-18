from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    #path('signin.html', views.signin, name='signin'),
    #path('attendence.html', views.attendence, name='attendence'),
    path('schedules.html', views.schedules, name='schedules'),
    #path('grades.html', views.grades, name='grades'),
    path('students.html', views.students, name='students'),
    path('adminlogin.html', views.adminlogin, name='adminlogin'),
    path('signout',views.signout, name="signout"),
]