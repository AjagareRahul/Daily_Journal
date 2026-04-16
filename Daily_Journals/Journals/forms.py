from django import forms
from .models import JournalEntry
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class JournalForm(forms.ModelForm):
    class Meta:
        model=JournalEntry
        fields=['title','mood','description']
        
class RegistrationForm(UserCreationForm):
    email=forms.EmailField(label="Enter Email")
    class Meta:
        model=User
        fields=['username','email','password1','password2']
