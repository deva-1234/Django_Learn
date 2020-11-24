from django import forms
from .models import blog1

class blogform(forms.ModelForm):
    class Meta:
        model=blog1
        fields=['Title','Name','Age']
