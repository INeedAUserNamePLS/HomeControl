from django.db import models


# Create your models here.
class Light(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    colour = models.CharField(max_length=200, default="#989898")
    brightness = models.IntegerField(default=100)
