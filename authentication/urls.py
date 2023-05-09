from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('index.html', views.home, name='home'),
    #path('signup.html', views.signup, name='signup'),
    path('signin.html', views.signin, name='signin'),
    path('cal.html', views.cal, name='cal'),
    path('schedules.html', views.schedules, name='schedules'),
    path('grades.html', views.grades, name='grades'),
    path('students.html', views.students, name='students'),
    path('rule.html',views.rule, name='rule'),
    path('signout',views.signout, name="signout"),
    path('about.html',views.about, name='about'),
]