import secrets
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    two_factor_code = models.CharField(max_length=20)
    secretToken = models.CharField(max_length=20)
    active = models.BooleanField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def createAccount(sender, instance, created, **kwargs):
    if created:
        userProfile = Account(user=instance)
        my_secure_rng = secrets.SystemRandom()
        code = my_secure_rng.randrange(10000, 99999)
        userProfile.two_factor_code = code
        userProfile.active = False
        userProfile.secretToken = secrets.token_urlsafe()
        userProfile.email = instance.email
        userProfile.save()
