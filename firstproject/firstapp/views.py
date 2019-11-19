from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def home(request):
    dict={'name':"This is a dict"}
    return render (request,'firstapp/index.html',context=dict)


def about(request):
    return HttpResponse("This is my about page")


def contact(request):
    return HttpResponse("Contact us page")


def form_view(request ):
    form = forms.Loginform
    return render (request,'firstapp/forms.html',{'form':form})