from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    summary=models.TextField()    
    def __str__(self):
        return  self.name

class Skill(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    

class Education(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    year=models.IntegerField()
    
    def __str__(self):
        return self.degree

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.title