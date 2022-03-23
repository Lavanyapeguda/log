from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def HOSPITAL(request):
    return render(request,"register/HOSPITAL.html")

def Home(request):
    return render(request,"register/home.html")

def pHome(request):
    return render(request,"register/phome.html")


#doctor's views

def Signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']

        if User.objects.filter(username=username):
            messages.error=(request,"username is already registered!please try some other username..!")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"Email is already Exis..!!")    
            return redirect('home')

        if len(username)>10:
            messages.error(request,"username mustbe under 10 chracters...!!")
            
        if password != password1:
            messages.error(request,"password didn't match..")

        if not username.isalnum():
            messages.error(request,"username must be alphanumeric ")
            return redirect('home')
        
         
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your Account has been created succesfully!!")
        return redirect('signin')
    return render(request,"register/signup.html")

def Signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"register/home.html",{"fname":fname})
        else:
            messages.error(request,"Bad credentials!!")
            return redirect('home')
    return render(request,"register/signin.html")
    


def Signout(request):

    logout(request)
    messages.success(request,"Logged out Successfully!!")
    return redirect('home')

#PATIENT view

def pSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']

        if User.objects.filter(username=username):
            messages.error=(request,"username is already registered!please try some other username..!")
            return redirect('phome')

        if User.objects.filter(email=email):
            messages.error(request,"Email is already Exis..!!")    
            return redirect('phome')

        if len(username)>10:
            messages.error(request,"username mustbe under 10 chracters...!!")
            
        if password != password1:
            messages.error(request,"password didn't match..")

        if not username.isalnum():
            messages.error(request,"username must be alphanumeric ")
            return redirect('phome')
        
         
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your Account has been created succesfully!!")
        return redirect('psignin')
    return render(request,"register/psignup.html")

def pSignin(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            fname1=user.first_name
            return render(request,"register/phome.html",{"fname":fname1})
        else:
            messages.error(request,"Bad credentials!!")
            return redirect('phome')
    return render(request,"register/psignin.html")
    


def pSignout(request):

    logout(request)
    messages.success(request,"Logged out Successfully!!")
    return redirect('phome')

