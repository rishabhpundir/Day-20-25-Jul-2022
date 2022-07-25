from django.shortcuts import render
from templates.forms import UploadForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    submitted = False
    form = UploadForm
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'form.html', {'form':form, 'submitted': submitted})
 

def form_data(request):
    return render(request, 'formdata.html')