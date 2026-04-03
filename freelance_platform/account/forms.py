from .models import Profile
from django import forms

# ModelForm automatically generates form fields based on the Profile model
class ProfileForm(forms.ModelForm):
    # Meta class specifies which model to use and which fields to include
    class Meta:
        model=Profile
        # Only bio and skills fields (user is set programmatically in view)
        fields=['bio','skills']