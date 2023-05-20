from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    two_factor_code = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def createAccount(sender, instance, created, **kwargs):
    if created:
        userProfile = Account(user=instance)
        userProfile.two_factor_code = "123"
        userProfile.save()

