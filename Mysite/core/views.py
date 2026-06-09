from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.db.models import Q

def home(request):
    student = [
    {'name': "Rahul", 'age': 22, 'city': 'Latur'}
]
    
    return render(request,'home.html',{'students':student})

def hero(request):
    return render(request,'hero.html')

def about(request):
    sort=request.GET.get('sort')
    query=request.GET.get('q')
    
    if query:
        students=Student.objects.filter(Q(name__icontains=query) | Q(city__icontains=query))
    else:
        if sort=="asc":
            students=Student.objects.all().order_by('id')
        elif sort=="desc":
            students=Student.objects.all().order_by('-id')
        else:
            students=Student.objects.all()
    
    return render(request,'about.html',{'students':students})

def contact(request):
    return render(request,'contact.html')
