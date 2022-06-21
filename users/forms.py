# users/forms.py
from http import client
from multiprocessing.connection import Client
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser, Client,Company

class ClientSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",) 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        return user
        
class CompanySignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        client = Client.objects.create(user=user)
        return user
        