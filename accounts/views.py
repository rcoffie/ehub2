from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name  = request.POST['last_name']
    username = request.POST['username']
    email    = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'username already Exits')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Sorry Email Already Exists')
          return redirect('register')
        else:
          user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
          user.save()
          messages.success(request,'User has been registered you can login now ')
          return redirect('login')
    else:
      messages.error(request, 'Password do not match')
      return redirct ('register')





    

  return render(request,'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      messages.success(request, 'you are now logged in')
      return redirect('dashboard')

    else:
      messages.error(request, 'invalid credentials')

  return render(request,'accounts/login.html')



def dashboard(request):
  return render(request,'accounts/dashboard.html')