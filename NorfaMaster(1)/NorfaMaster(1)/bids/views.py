from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 

from .models import Bid

class BidListView(ListView):
    model = Bid
    template_name = 'bid_list.html'
    login_url = 'login' 

class BidDetailView(DetailView):
    model = Bid
    template_name = 'bid_detail.html'
    login_url = 'login' 


class BidCreateView(LoginRequiredMixin,CreateView):
    model = Bid
    template_name = 'bid_new.html'
    fields = ('service','time','phone_number','adress','worker','company')
    login_url = 'login' 
    
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

