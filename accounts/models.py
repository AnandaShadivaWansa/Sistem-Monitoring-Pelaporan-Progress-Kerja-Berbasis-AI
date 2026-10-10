from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('personel', 'Personel'),
        ('spv', 'SPV'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='personel')

    def __str__(self):
        return f"{self.username} ({self.role})"