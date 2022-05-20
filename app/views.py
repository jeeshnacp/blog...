from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from app.form import userregister, loginRegister
from app.models import user


def home(request):
    return render(request,'home.html')

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
               return redirect('admin_home')
            elif user.is_user:
                return  redirect('user_home')

        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

def user_register(request):
    user_form=userregister()
    login_form=loginRegister()
    if request.method=='POST':
        user_form=userregister(request.POST)
        login_form=loginRegister(request.POST)
        if user_form.is_valid() and login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            user = user_form.save(commit=False)
            user.user = user
            user.save()
            messages.info(request, 'Registration Successfull')
            return redirect('login')

    return render(request, 'signup.html', {'login_form': login_form, 'user_form': user_form})

def logout_view(request):
    logout(request)
    return redirect('login')

def view_user(request):
    data=user.objects.all()
    return render(request,'view_user.html',{'data':data})
