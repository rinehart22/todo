
from .models import * 
from django.forms import ModelForm
from django.forms import ModelForm, forms
from django import forms
#from django.forms import forms

class PersonForm(ModelForm):
    
    class Meta:
        model = Person
        fields = "__all__"




