from django.db import models
from datetime import datetime 
from RealtorApp import Realtor
#from django.db.models import CharField
#from django.db.models import TextField
# Create your models here.
class demomodel(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    prize = models.models.IntegerField()
    bedroom = models.models.IntegerField()
    Bathrooms = models.models.models.models.models.DecimalField( max_digits=4, decimal_places=1)
    Garage = models.models.IntegerField(default=0)
    sqft = models.models.IntegerField()
    lotsize = models.models.models.DecimalField( max_digits=5, decimal_places=1)
    image_Main = models.ImageField(upload_to='pics')
    Main_1 = models.ImageField(upload_to='pics',blank=true)
    Main_2 = models.ImageField(upload_to='pics',blank=true)
    Main_3 = models.ImageField(upload_to='pics',blank=true)
    Main_4 = models.ImageField(upload_to='pics',blank=true)
    Main_5 = models.ImageField(upload_to='pics',blank=true)
    Main_6 = models.ImageField(upload_to='pics',blank=true)
    is_published = models.BooleanField(default=true)
    list_date = models.DateTimeField(default=datetime.now(),blank=true)
def __str__(self):
    return self.title
