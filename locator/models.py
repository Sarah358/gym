from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Location(models.Model): 
   name = models.CharField(max_length=250) 
   address = models.TextField() 
   latitude = models.FloatField() 
   longitude = models.FloatField() 
   payments = models.FloatField()
   phonenumber = models.FloatField()

   def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=50)
    gymname = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Booking(models.Model):

    name = models.CharField(max_length=50)
    username = models.ForeignKey(to=User, on_delete=models.CASCADE)
    package =  models.CharField(max_length=50)
    gymname =  models.CharField(max_length=250)
    amount = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    date = models.DateField(default=now)


    def __str__(self):
        return self.name

