from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request,"accounts/notes.html")
    
    else:
        if request.method=="POST":
            email=request.POST["email"]
            password=request.POST["password"]
            user=auth.authenticate(username=email,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect("notes")
            else:
                messages.info(request,"Invalid Credentials")
                return redirect('/')
        else:
            return render(request,'accounts/login.html')
        

def register(request):
    if request.method=='POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        
        if password==password2:
            if User.objects.filter(username=email).exists():
                messages.info(request,'Account with the given email already exists, please try to login instead.')
                return redirect('register')
            else:
                user=User.objects.create_user(username=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html')
        
    
    
def notes(request):
    return render(request, 'accounts/notes.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
