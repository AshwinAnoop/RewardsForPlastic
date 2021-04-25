from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import extendeduser,scrapshop,locality
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
        if request.method=='POST':
            place = request.POST['place']
            shopobj = scrapshop.objects.filter(locality = place)
            localities = locality.objects.all()
            return render(request,'home.html',{'shopobj' : shopobj, 'localities' : localities})

        else:
            shopobj = scrapshop.objects.all()
            localities = locality.objects.all()
            return render(request,'home.html',{'shopobj' : shopobj, 'localities' : localities})


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')


    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['phno']
        location = request.POST['locality']
        address = request.POST['address']
        password1 = request.POST['password']
        password2 = request.POST['retypepassword']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=email,email=email,password=password1,first_name=username)
                newextendeduser = extendeduser(mobile=mobile, user=user, locality_id=location, address=address)
                newextendeduser.save();
                print('user created')
                return redirect('login')                
        else:
            messages.info(request,'Passwords not matching')
            return redirect('signup')

        return redirect('/')
        
    else:
        localities = locality.objects.all()
        return render(request,'signup.html',{'localities' : localities})


def shopoverview(request):
    shopid = request.GET['shopid']
    shopdetails = scrapshop.objects.filter(id=shopid)
    return render(request,'shopoverview.html',{'shopdetails' : shopdetails})