from django.db import models

# Create your models here.
class Stud(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    attper=models.IntegerField()
    gpa=models.FloatField()
    
    def __str__(self):
        return self.sid

class details(models.Model):
    rno=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.rno