from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import RegisterUserForm, ChangePasswordForm


# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, ("There was an Error Logging In, Try Again ..."))
            return redirect("login")
    else:
        return render(request, "authenticate/login.html", {})


def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect("twoFactor")
        else:
            messages.error(request, ("Registration failed"))
    form = RegisterUserForm()
    return render(request, "authenticate/register.html", {"form": form})


@login_required
def twoFactor(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, ("Registration Successful"))
            return redirect("index")
    else:
        return render(request, "authenticate/twoFactor.html", {})


@login_required
def logoutUser(request):
    logout(request)
    messages.info(request, ("User was logged out"))
    return redirect("login")


@login_required
def manageAccount(request):
    return render(request, "account/view.html", {"account": request.user})


@login_required
def changePassword(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            form.save()
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 == password2:
                request.user.set_password(password2)
                request.user.save()
                messages.success(request, ("Password changed"))
                return redirect("manageAccount")
            else:
                messages.error(request, ("The two passwords did not match"))
        else:
            messages.error(request, ("Password did not match the required Strength"))
        return redirect("changePassword")
    else:
        form = ChangePasswordForm(request.user)
        return render(request, "account/changePassword.html", {"form": form})
