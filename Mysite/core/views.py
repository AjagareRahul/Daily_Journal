from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    student = [
    {'name': "Rahul", 'age': 22, 'city': 'Latur'}
]

    return render(request,'home.html',{'students':student})
   # return HttpResponse("Django Started")

def about(request):
    students=Student.objects.filter(age=22)
    
    #student=Student.objects.all()
    return render(request,'about.html',{'students':students})
    #return HttpResponse("About Page")
    '''student=[
        {'name':'Rahul','sirname':'Ajagare','age':22},
        {'name':'Danny','sirname':'Ajagare','age':23},
    ]
    '''

def contact(request):
    return render(request,'contact.html')
