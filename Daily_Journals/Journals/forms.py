from django import forms
from .models import JournlEntry
class JournalForm(forms.ModelForm):
    class Meta:
        model=JournlEntry
        fields=['title','mood','description']