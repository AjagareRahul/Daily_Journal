from django.shortcuts import render
from django.http import HttpResponse
from Hub.models import Student

def home(request):
    students=Student.objects.all()
    return render(request,'home.html',{'students':students})
   
   
   
   # return HttpResponse("This is home page")
 
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about page")




