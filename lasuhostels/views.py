from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render (request, 'lasuhostels/index.html')

def hostels(request):
    return render(request, 'lasuhostels/project-detail.html')

def advertise(request):
    return render(request, 'lasuhostels/contact.html')

def submit(request):
    return HttpResponseRedirect('create')

def hostelcreator(request):
    return render(request, 'lasuhostels/hostelcreator.html')
