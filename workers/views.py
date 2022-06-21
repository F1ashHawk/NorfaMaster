from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy 

from .models import Worker

class WorkerListView(ListView):
    model = Worker
    template_name = 'worker_list.html'
    login_url = 'login' 

class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'worker_detail.html'
    login_url = 'login' 

class WorkerUpdateView(UpdateView): 
    model = Worker
    fields = ('title','schedule','rating')
    template_name = 'worker_edit.html'
    login_url = 'login' 

    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WorkerDeleteView(DeleteView):    
    model = Worker
    template_name = 'worker_delete.html'
    success_url = reverse_lazy('worker_list')
    login_url = 'login' 
    
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WorkerCreateView(LoginRequiredMixin,CreateView):
    model = Worker
    template_name = 'worker_new.html'
    fields = ('title','schedule','rating')
    login_url = 'login' 
    
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

