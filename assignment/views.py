from django.shortcuts import render
from .models import Family
from django import forms

# Create your views here.
def family(request):
    family = Family.objects.all()
    context ={
        'family':family
    }
    return render(request,'listing_family_members.html', context)
