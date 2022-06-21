# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ClientSignUpForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = ClientSignUpForm
    model = CustomUser
    list_display = ['email', 'username', 'is_client','is_company', 'age', ] # new

admin.site.register(CustomUser, CustomUserAdmin)