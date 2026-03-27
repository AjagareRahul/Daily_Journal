from django.shortcuts import render,redirect
from resume.models import Profile,Education
from resume.forms import ProfileForm,EducationForm

# Display all profiles on the home page
def home(request):
    profile=Profile.objects.all()
    education=Education.objects.all()
    
    return render(request,'home.html',{'profile':profile,'education':education})

# Handle creation of a new profile with education details
def create(request):
    form=ProfileForm()
    education=EducationForm()

    if request.method=='POST':
        # Bind submitted data to both forms
        form=ProfileForm(request.POST)
        education=EducationForm(request.POST)

        if form.is_valid() and education.is_valid():
            # Save profile first to get its primary key
            profile=form.save()
            # Save education without committing so we can attach the profile FK
            edu=education.save(commit=False)
            edu.profile=profile
            edu.save()

            return redirect('home')

    return render(request,'add_data.html',{'form':form,'education':education})