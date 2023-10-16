from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return render(request,'login.html')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fname = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        print("here")
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('/register/')
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=last_name,password=password,email=email)
                user.save()
                return redirect('/credentials/login')
        else:
            messages.info(request,"Passwords not matched")
            return render(request,'register.html')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')