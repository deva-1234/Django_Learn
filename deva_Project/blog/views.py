from django.shortcuts import render
from django.http import HttpResponse
from .models import blog1
from .forms import blogform

def home(request):
    con=blogform()
    context={'posts':con}
    return render(request,'blog/deva.html',context)
    

# Create your views here.
