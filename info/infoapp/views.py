from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from.forms import *
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def home(request):
    return render(request,"index.html")


def register(request):
    if request.method == 'POST':
        formdata = register_form(request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.info(request,"Registered Successfully")
            return HttpResponseRedirect('/register/')
    else:
        formdata = register_form()
    return render(request,'register.html',{"formdata":formdata})



def signup(request):
    if request.method == 'POST':
        form1 = signup_form(request.POST)
        if form1.is_valid():
            username1 = form1.cleaned_data['username']
            email1 = form1.cleaned_data['email']
            first_name1 = form1.cleaned_data['first_name']
            last_name1 = form1.cleaned_data['last_name']
            password1 = form1.cleaned_data['password']
            if User.objects.filter(email=email1).exists():
                messages.info(request,"Email ID is Already register!")
                return HttpResponseRedirect('/signup/')
            else:
                user = User.objects.create_user(username=username1,first_name=first_name1,last_name=last_name1,email=email1,password=password1)
                user.save()
                messages.success(request,'User registration Succsessfully')
                return HttpResponseRedirect('/index/')
    else:
        form1 = signup_form()
    return render(request,'signup.html',{'frm':form1})



def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"welcome.html",{"myusername":username})
        else:
            messages.info(request,"invalid Input")
            return redirect("/login/")

    return render(request,"login.html")