from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


def register(request):
    
    try:
        
        if request.method == 'POST':
            data = request.POST
            username = data['username']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            password1 = data['password1']
            password2 = data['password2']
            
            if User.objects.filter(username =username).exists():
                return messages.error('User already exists.')

            if password1 == password2:
                User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=make_password(password1)
                )
                return redirect('login')
            else:
                # Handle password mismatch
                pass
    except ValueError:
        messages.error('Invalid Input')
        
    except Exception as e:
        messages.error('An Unexpected Error has occur.')
        
    return render(request, 'register.html')


@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        pwd = request.POST['password']
        
        user =authenticate(request,username = username ,password = pwd)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect("home")
        else: 
            messages.error(request,'Invalide Username or Password.')
            return redirect('login')
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
