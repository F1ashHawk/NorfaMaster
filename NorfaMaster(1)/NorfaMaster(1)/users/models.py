from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    