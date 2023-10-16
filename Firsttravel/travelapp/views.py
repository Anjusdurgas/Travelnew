from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Place
from . models import Team, User
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()#fetches all dat from Place table
    return render(request,"index.html",{'result':obj,'result1':obj1})

# def demo1(request):
#     obj1=Team.objects.all()
#     return render(request,"index.html",{'result1':obj1})
#ORM -->    Object–relational mapping

# def regUser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         firstname=request.POST.get('firstname')
#         lastname=request.POST.get('lastname')
#         email=request.POST.get('email')
#         password=request.POST.get['password']
#         password1=request.POST.get['password1']
#         print("I am in travel register")
#         if (password==password1):
#             user=User(username=username,firstname=firstname,lastname=lastname,email=email,)
#             user.save()
#             return redirect('/')
#     return render(request,"register.html")
