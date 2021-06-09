from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hostels', views.hostels, name="hostels"),
    path('advertise', views.advertise, name="Advertise"),
    path('submit', views.submit, name="submit"),
    path('create', views.hostelcreator, name="create"),
    path('creating', views.creating, name='creating')
]

