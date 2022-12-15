from django.shortcuts import render
from testapp import views
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import Employee
def register(request):
 if request.method=="POST":
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username=request.POST['username']
    email=request.POST['email']
    password1=request.POST['password1']
    password2=request.POST['password2']
    if password1==password2:
      if User.objects.filter(username=username).exists():
        print ('Username Taken')
      elif User.objects.filter(email=email).exists():
        print ('Email Taken')
      else:
       user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
       print("User Created")
       user.save();
       
    else:
     print("Password not matched")
    return render(request,'pages/register.html') 
 else:
  return render(request,'pages/register.html')  
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password'] 
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
          print("user Found")
          return views.home(request)
        else:
         print("Wrong Credentials")
         return render(request,'pages/login.html')

    else:
      return render(request,'pages/login.html')
def logout(request):
  auth.logout(request)
  return views.home(request)
  