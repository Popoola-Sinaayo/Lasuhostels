from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Hostels
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
def creating(request):
    if request.method == 'POST':
        Type = request.form.get('type')
        Description = request.form.get('Description')
        Initial_Price = request.form.get('PriceInit')
        Price_Subs = request.form.get('PriceSubs')
        Location = request.form.get('Location')
        hostel = Hostels(Name=Type, Description=Description, Location=Location, Price=Initial_Price, Subsequent_Price=Price_Subs, Agent_Name=Name)