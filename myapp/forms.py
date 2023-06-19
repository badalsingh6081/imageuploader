from django import forms
from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title','file']
        labels= {'file':''}
        widgets={
            'title':forms.TextInput(attrs={'class':'myclass form-control','placeholder':'Title'}),
            'file':forms.FileInput(attrs={'class':'myclass form-control','placeholder':'First Name'}),

        }
