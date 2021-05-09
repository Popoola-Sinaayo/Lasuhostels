from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Agent(models.Model):
    Name = models.CharField(max_length=99999)
    Number = models.IntegerField(default=0)
class Hostels(models.Model):
    Name = models.CharField(max_length=1000)
    Description = models.CharField(max_length=100000000)
    Location = models.CharField(max_length=100000000)
    Price = models.IntegerField(default=0)
    Subsequent_Price = models.IntegerField(default=0)
    Agent_Name = models.CharField(max_length=1000000, default='user')