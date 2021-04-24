from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
        if request.method=='POST':
            place = request.POST['place']
            lotobjs = parkinglot.objects.filter(locality = place)
            localities = locality.objects.all()
            return render(request,'home.html',{'lotobjs' : lotobjs, 'localities' : localities})

        else:
            return render(request,'home.html')