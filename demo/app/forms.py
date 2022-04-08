from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['title','project','description']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'project':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
            'description':forms.TextInput(attrs={'class':'form-control p-2 mt-2'}),
        }
