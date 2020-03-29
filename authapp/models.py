from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.

def det_expires_datetime():
    return now() + timedelta(hours=48)

class ShopUser(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        default=det_expires_datetime()
    )

    def __str__(self):
        return self.username

    def is_activation_key_expired(self):
        return now() > self.activation_key_expires
