from django.shortcuts import render,get_object_or_404,redirect
from .models import JournalEntry
from django.contrib.auth.forms import AuthenticationForm 
from Journals.forms import JournalForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.
@login_required
def home(request):
    journals=JournalEntry.objects.all().order_by('-create_at')
    return render(request,'home.html',{'journals':journals, 'user':request.user})

def registration(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    return render(request,'register.html',{'form':form})

def user_login(request):
    form=AuthenticationForm(request,data=request.POST or None)
    if request.method=='POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('home')
    return render(request, 'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('login')

def create_journals(request):
    if request.method=='POST':
        form=JournalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=JournalForm()
    return render(request,'add_Journal.html',{'forms':form})


def update_journal(request,id):
    entry=get_object_or_404(JournalEntry,id=id)
    if request.method=='POST':
        form=JournalForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=JournalForm(instance=entry)
    return render(request,'update_journal.html',{'forms':form})

def delete_entry(request,id):
    entry=get_object_or_404(JournalEntry,id=id)
    entry.delete()
    return redirect('home')
    
