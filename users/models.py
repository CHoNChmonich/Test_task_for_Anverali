from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class User(AbstractUser):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('freelancer', 'Freelancer'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    position = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    class Meta:
        db_table = 'user'
        verbose_name='Пользователя'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return self.username