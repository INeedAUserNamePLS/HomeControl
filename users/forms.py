from typing import Any
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            "username",
            "firstName",
            "lastName",
            "email",
            "password1",
            "password2",
        ]

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = [
            "password1",
            "password2",
        ]
