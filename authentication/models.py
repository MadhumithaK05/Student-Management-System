from django.db import models

# Create your models here.
class Stud(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    attper=models.IntegerField()
    gpa=models.FloatField()
    
    def __str__(self):
        return f"{self.sid}({self.gpa})"
