from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Light(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    colour = models.CharField(max_length=200, default="#989898")
    brightness = models.IntegerField(default=100)

class User(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
