from django.urls import path

from . import views

urlpatterns = [
    path("login_user", views.loginUser, name="login"),
    path("logout_user", views.logoutUser, name="logout"),
    path("register_user", views.registerUser, name="register"),
    path("reset_password", views.resetPassword, name="resetPassword"),
    path("manage_account", views.manageAccount, name="manageAccount"),
    path("delete_user", views.deleteAccount, name="deleteAccount"),
    path("two_factor", views.twoFactor, name="twoFactor"),
    path("activation/<int:code>", views.activation, name="activation"),
    path("change_password", views.changePassword, name="changePassword"),
]
