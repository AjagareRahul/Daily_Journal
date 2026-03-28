from django import forms
from resume.models import Profile,Skill,Project,Education

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','phone','summary']
        
class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=['degree','college','year']

class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields=['name']
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['title','description']