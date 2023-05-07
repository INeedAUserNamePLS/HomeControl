from django.urls import path

from . import views

urlpatterns = [
    path('login_user', views.loginUser, name="login"),
    path('register_user', views.registerUser, name="register"),
]