from django import forms
from django.forms import ModelForm
from app3.models import Upload

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ("image",)