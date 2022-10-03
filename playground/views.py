from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
 
# relative import of forms
 
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "hello.html", context)