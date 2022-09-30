from django.shortcuts import render, redirect

from app.forms import PersonForm

# Create your views here.
from .models import * 
from .forms import *


def home(request):
    all_objs = Person.objects.all()
    return render(request, 'home.html', {'all':all_objs})


def create(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    context ={'form':form}
    return render(request, 'create.html', context)

def read(request, id):
    
    get_one_obj = Person.objects.get(pk=id)
    return render(request, 'read.html', {'all':get_one_obj})



def delete(request, id):
    Person.objects.get(pk=id).delete()
    return render(request, 'delete.html') 


def update(request, id):  
    z = Person.objects.get(pk=id)
    form = PersonForm(instance=z) 
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=z)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update.html', context)
