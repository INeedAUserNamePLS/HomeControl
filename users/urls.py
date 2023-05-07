from django.urls import path

from . import views

urlpatterns = [
    path('login_user', views.loginUser, name="login"),
    path('logout_user', views.logoutUser, name="logout"),
    path('register_user', views.registerUser, name="register"),

]