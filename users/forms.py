from typing import Any
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
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
