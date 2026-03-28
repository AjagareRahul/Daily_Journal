from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from resume.models import Profile, Education, Skill, Project
from resume.forms import ProfileForm, EducationForm, SkillForm, ProjectForm


def home(request):
    profile = Profile.objects.all()
    return render(request, 'home.html', {'profile': profile})


def create(request):
    form = ProfileForm()
    education = EducationForm()
    skill = SkillForm()
    project = ProjectForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        education = EducationForm(request.POST)
        skill = SkillForm(request.POST)
        project = ProjectForm(request.POST)

        if form.is_valid() and education.is_valid() and skill.is_valid() and project.is_valid():
            profile = form.save()

            edu = education.save(commit=False)
            edu.profile = profile
            edu.save()

            sk = skill.save(commit=False)
            sk.profile = profile
            sk.save()

            proj = project.save(commit=False)
            proj.profile = profile
            proj.save()

            messages.success(request, 'Resume created successfully!')
            return redirect('home')

    return render(request, 'add_data.html', {
        'form': form, 'education': education, 'skills': skill, 'project': project
    })


def update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    edu = Education.objects.filter(profile=profile).first()
    sk = Skill.objects.filter(profile=profile).first()
    proj = Project.objects.filter(profile=profile).first()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        education = EducationForm(request.POST, instance=edu)
        skill = SkillForm(request.POST, instance=sk)
        project = ProjectForm(request.POST, instance=proj)

        if form.is_valid() and education.is_valid() and skill.is_valid() and project.is_valid():
            profile = form.save()

            edu_obj = education.save(commit=False)
            edu_obj.profile = profile
            edu_obj.save()

            sk_obj = skill.save(commit=False)
            sk_obj.profile = profile
            sk_obj.save()

            proj_obj = project.save(commit=False)
            proj_obj.profile = profile
            proj_obj.save()

            messages.success(request, 'Resume updated successfully!')
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
        education = EducationForm(instance=edu)
        skill = SkillForm(instance=sk)
        project = ProjectForm(instance=proj)

    return render(request, 'update_data.html', {
        'form': form, 'education': education, 'skills': skill, 'project': project, 'pk': pk
    })


def delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Resume deleted successfully!')
        return redirect('home')
    return render(request, 'confirm_delete.html', {'profile': profile})
