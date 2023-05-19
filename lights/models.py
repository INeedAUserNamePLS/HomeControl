from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Light(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    colour = models.CharField(max_length=200, default="#989898")
    brightness = models.IntegerField(default=100)


class Broker(models.Model):
    name = models.CharField(max_length=200)
    server = models.CharField(max_length=200)
    port = models.IntegerField(null=True, blank=True)
    keepAlive = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
