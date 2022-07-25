from django import forms
from django.forms import ModelForm
from FUApp.models import Upload

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('name', 'age', 'gender', 'profile_pic', 'desc')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'age' : forms.TextInput(attrs={'class': 'form-control'}),
            'gender' : forms.TextInput(attrs={'class': 'form-control'}),
            'desc' : forms.TextInput(attrs={'class': 'form-control'}),
        }