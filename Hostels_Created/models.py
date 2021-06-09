from django.db import models

# Create your models here.

'''
class Agent(models.Model):
    Name = models.CharField(max_length=99999)
    Number = models.IntegerField(default=0)'''

class Created(models.Model):
    No = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=1000)
    Description = models.CharField(max_length=100000000)
    Location = models.CharField(max_length=100000000)
    Price = models.IntegerField(default=0)
    Subsequent_Price = models.IntegerField(default=0)
    Agent = models.CharField(max_length=10000, default='Agent')
    