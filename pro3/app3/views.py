from django.shortcuts import render
from templates.form import UploadForm

# Create your views here.

def imgup(request):
    form = UploadForm
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'img.html', {'form':form})
