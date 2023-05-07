from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,("There was an Error Logging In, Try Again ..."))
            return redirect('login')
    else:
        return render(request,'authenticate/login.html', {})

def registerUser(request):
    return render(request,'authenticate/register.html', {})

def logoutUser(request):
    logout(request)
    messages.info(request,("User was logged out"))
    return redirect('login')
