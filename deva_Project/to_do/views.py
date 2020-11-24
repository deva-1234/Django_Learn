from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import todo
# Create your views here.
def hom(request):
    post=todo.objects.all().order_by('-Date_id')

    return render(request,'todo/deva.html',{'posts':post})

def Todoview(request):
    print(request.POST['add-text'])
    post=todo.objects.all().order_by('-Date_id')
    if request.method=='POST':
        todo.objects.create(text=request.POST['add-text'])    
        return HttpResponseRedirect('/')
    
    
    return HttpResponseRedirect('/')

def delview(request,post_id):

    if request.method=='POST':
        todo.objects.get(id=post_id).delete()    
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def updateview(request,post_id):
    
    return render(request,'todo/update.html')

def updatesview(request,post_id):
    if request.method=='POST':
        print(post_id)
        todo.objects.filter(id=post_id).update(text=request.POST['add-text1'])
        post=todo.objects.all().order_by('-Date_id')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
