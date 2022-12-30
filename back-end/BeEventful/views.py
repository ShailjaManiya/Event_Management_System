from django.http.response import HttpResponse
from django.shortcuts import render,redirect

#from django.contrib.auth.decorators import 
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import ExtendedUserCreationForm, ProfileForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')   

def services(request):
    return render(request,'services.html') 

def registration(request):
    if request.method=='POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user=form.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            profile.save()
            return redirect('login')
    else:
        form=ExtendedUserCreationForm()
        profile_form=ProfileForm()

    context={'form':form, 'profile_form':profile_form}
    return render(request,'registration.html',context)

def registration_new(request):
    return render(request,'registration_new.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'After_login.html',{'username':username})
        else:
            messages.info(request,'invalid credentials please try again')
            return redirect('login')
    else:
        return render(request,'login.html')

def Admin_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser==True:
                auth.login(request,user)
                return render(request,'AdminPage.html',{'username':username})
        else:
            messages.info(request,'invalid credentials please try again')
            return redirect('Admin_login')
    else:
        return render(request,'Admin_login.html')

def After_login(request):
    return render(request,'After_login.html')

def AdminPage(request):
    return render(request,'AdminPage.html')

def logout(request):
    auth.logout(request)
    return redirect('home')