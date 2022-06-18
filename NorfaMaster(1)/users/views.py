from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ClientSignUpForm,CompanySignUpForm
from .models import CustomUser,Client,Company

class ClientSignUpView(CreateView):
    model = CustomUser
    form_class = ClientSignUpForm
    template_name = 'client_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class CompanySignUpView(CreateView):
    model = CustomUser
    form_class = CompanySignUpForm
    template_name = 'company_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')