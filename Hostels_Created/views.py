from django.shortcuts import render
from .models import Created
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    count = Created.objects.count()
    h = Created.objects.all()
    return render (request, 'index.html', context={
        'Hostels': h,
        'count': count
    })

def hostels(request):
    h = Created.objects.all
    return render(request, 'project-detail.html', context={
        'Hostel': h
    })

def advertise(request):
    return render(request, 'contact.html')

def submit(request):
    return HttpResponseRedirect('create')

def hostelcreator(request):
    return render(request, 'hostelcreator.html')

def creating(request):
    if request.method == 'POST':
        Type = request.POST['Type']
        Description = request.POST['Description']
        Initial_Price = request.POST['PriceInit']
        Price_Subs = request.POST['PriceSubs']
        Location = request.POST['Location']
        h = Created.objects.create(Name=Type, Description=Description, Location=Location, Price=Initial_Price, Subsequent_Price=Price_Subs)
        h.save()
        return HttpResponseRedirect('/')


def view_Hostel(request):
    return None