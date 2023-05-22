import secrets
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Account
from users.forms import RegisterUserForm, ChangePasswordForm, TwoFactorForm
from lights import mails


def active_check(user):
    account = Account.objects.get(user=user)
    return account.active


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
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect("twoFactor")
        else:
            messages.error(request, form.errors)
    form = RegisterUserForm()
    return render(request, "authenticate/register.html", {"form": form})


def resetMail(request):
    resetCode = secrets.token_urlsafe()
    if request.method == "POST":
        post_email = request.POST["email"]
        if Account.objects.filter(email=post_email).exists():
            account = Account.objects.get(email=post_email)
            account.secretToken = resetCode
            account.save()
            mails.sendReset(post_email, account.id, resetCode, request.get_host())
        messages.success(request, ("Password recovery mail sent, if Account exists"))
        return render(request, "account/resetMail.html", {})
    else:
        return render(request, "account/resetMail.html", {})


@login_required
def twoFactor(request):
    account = Account.objects.get(user=request.user)
    accountCode = account.two_factor_code
    if request.method == "POST":
        form = TwoFactorForm(request.POST)
        if form.is_valid():
            code = request.POST["two_factor_code"]
            if code == accountCode:
                account.active = True
                account.save()
                messages.success(request, ("Registration Successful"))
                return redirect("index")
            else:
                messages.error(request, ("Wrong Code"))
                return redirect("twoFactor")
        else:
            messages.error(request, form.errors)
            return redirect("twoFactor")
    else:
        mails.sendTwoFactor(request.user.email, accountCode, request.get_host())
        return render(request, "authenticate/twoFactor.html", {})


@login_required
@user_passes_test(active_check)
def logoutUser(request):
    logout(request)
    messages.info(request, ("User was logged out"))
    return redirect("login")


@login_required
@user_passes_test(active_check)
def manageAccount(request):
    return render(request, "account/view.html", {"account": request.user})


@login_required
@user_passes_test(active_check)
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
                messages.error(request, form.errors)
        else:
            # ToDo
            messages.error(request, form.errors)
        return redirect("changePassword")
    else:
        form = ChangePasswordForm(request.user)
        return render(request, "account/changePassword.html", {"form": form})


@login_required
def activation(request, code):
    secretToken = secrets.token_urlsafe()
    if code == request.user.two_factor_code:
        request.user.active = True
        messages.success(request, ("Registration Successful"))
        return redirect("index")
    else:
        messages.error(request, ("Wrong Code"))
        return redirect("twoFactor")


@login_required
@user_passes_test(active_check)
def deleteAccount(request):
    try:
        request.user.delete()
        messages.success(request, "The user is deleted")
    except Exception as e:
        messages.error(request, e)
        return render(request, "account/view.html", {"account": request.user})
    return redirect("login")


def passwordRecovery(request, userid, token):
    account = Account.objects.get(id=userid)
    if request.method == "POST":
        form = ChangePasswordForm(request.user)
        if form.is_valid():
            form.save()
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 == password2:
                if password1 == None:
                    messages.error(request, ("Password is empty"))
                else:
                    account.set_password(password2)
                    account.save()
                    messages.success(request, ("Password changed"))
                    return redirect("login")
            else:
                messages.error(request, ("Passwords did not match"))
        else:
            # ToDo
            messages.error(request, form.errors)
    else:
        if account.secretToken != token:
            messages.error(request, ("Wrong token"))
            redirect("resetMail")    
    form = ChangePasswordForm(request.user)
    return render(
        request,
        "account/resetPassword.html",
        {"form": form, "userid": userid, "token": token},
    )
