from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('cal.html', views.cal, name='cal'),
    path('schedules.html', views.schedules, name='schedules'),
    path('grades.html', views.grades, name='grades'),
    path('students.html', views.students, name='students'),
    path('rule.html',views.rule, name='rule'),
    path('about.html',views.about, name='about'),
]