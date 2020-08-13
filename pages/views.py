from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import demomodel
k = demomodel.objects.all()
def home(request):
    return render(request ,'home.html',{'data':k})
