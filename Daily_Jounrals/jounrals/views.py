from django.shortcuts import render,redirect
from django.db.models import Q
from jounrals.models import JournalEntry
from datetime import datetime
# Create your views here.

def home(request):
    entries=JournalEntry.objects.all().order_by('-date')
    query=request.GET.get('q', '')
    mood=request.GET.get('mood', '')
    date_filter=request.GET.get('date', '')
    
    # Text search
    if query:
        entries=entries.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    # Mood filter
    if mood:
        entries=entries.filter(mood=mood)
    
    # Date filter
    if date_filter:
        entries=entries.filter(date__date=date_filter)
    
    return render(request,'home.html',{'entries':entries, 'query':query, 'mood':mood, 'date_filter':date_filter})

def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        mood=request.POST.get('mood')
        description=request.POST.get('description')
        JournalEntry.objects.create(
            title=title,
            mood=mood,
            description=description)
        return redirect('home')      
    return render(request,'add_page.html')

def update(request,id):
    entry=JournalEntry.objects.get(id=id)
    if request.method=='POST':
        entry.title=request.POST.get('title')
        entry.mood=request.POST.get('mood')
        entry.description=request.POST.get('description')
        entry.save()
        return redirect('home')
    return render(request,'update_entry.html', {'entry':entry})

def delete(request,id):
    entry=JournalEntry.objects.get(id=id)
    entry.delete()
    return redirect('home')