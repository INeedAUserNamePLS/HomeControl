from django.db import models


# Create your models here.
class Light(models.Model):
    name = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    colour = models.CharField(max_length=200)
    brightness = models.IntegerField(default=100)
