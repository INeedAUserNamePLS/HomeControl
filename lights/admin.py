from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Light,Broker

admin.site.register(Light)
admin.site.register(Broker)
admin.site.unregister(Group)