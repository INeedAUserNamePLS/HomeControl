from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User

from users.models import Account


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

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
            "new_password1",
            "new_password2",
        ]


class TwoFactorForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            "two_factor_code",
        ]
