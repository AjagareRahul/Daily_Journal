from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    age=models.IntegerField()
    college=models.CharField(max_length=100)
    
    def __str__(self):
        return f"fName:{self.fname}, lName:{self.lname}"
    
    