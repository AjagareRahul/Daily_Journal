from django.shortcuts import render
from django.http import HttpResponse
from Hub.models import Student
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):

    students = Student.objects.all()

    # pagination
    paginator = Paginator(students, 3)   # 3 per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'home.html', {'students': students})
'''
    query = request.GET.get('q')
    if query:
        students = students.filter(
            Q(fname__icontains=query) | Q(college__icontains=query)
        )

    sort = request.GET.get('sort')
    if sort == "asc":
        students = students.order_by('age')
    elif sort == "desc":
        students = students.order_by('-age')

    return render(request, 'home.html', {'students': students})'''
   
   
   
   # return HttpResponse("This is home page")
 
def about(request):
    student=Student.objects.filter(age=22).first()
    return render(request,'about.html',{'student':student})


    #return HttpResponse("This is about page")




