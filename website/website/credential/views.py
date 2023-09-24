from django.contrib import messages, auth
from django.contrib.auth.models import User

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
            messages.info(request,'Please enter registered username/password')
            return redirect('login')
    return render(request,'sign.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
     if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if User.objects.filter(username=username).exists():
            messages.info(request, "User already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already Exists")
            return redirect('register/register')
        elif password == cpassword:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password, email=email)
            user.save();
            messages.info(request, "User created Successfully")
            print('User Created')
            return redirect('login')
        else:
            messages.info(request, "Password doesnot match")
            return redirect('register')

     return render(request, 'sign.html')
