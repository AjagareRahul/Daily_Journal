from django.shortcuts import render,get_object_or_404,redirect
from .models import JournlEntry
from Journals.forms import JournalForm
# Create your views here.

def home(request):
    journals=JournlEntry.objects.all().order_by('-create_at')
    return render(request,'home.html',{'journals':journals})

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
    entry=get_object_or_404(JournlEntry,id=id)
    if request.method=='POST':
        form=JournalForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=JournalForm(instance=entry)
    return render(request,'update_journal.html',{'forms':form})

def delete_entry(request,id):
    entry=get_object_or_404(JournlEntry,id=id)
    entry.delete()
    return redirect('home')
    