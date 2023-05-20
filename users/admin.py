from django.contrib import admin
from django.contrib.auth.models import User
from .models import Account


class AccountInline(admin.StackedInline):
    model = Account


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [AccountInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
