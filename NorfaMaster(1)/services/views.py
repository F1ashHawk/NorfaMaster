from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy 

from .models import Service

class ServicesListView(ListView):
    model = Service
    template_name = 'services_list.html'
    login_url = 'login' 

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    login_url = 'login' 

class ServiceUpdateView(UpdateView): 
    model = Service
    fields = ('title','schedule','body','cost')
    template_name = 'service_edit.html'
    login_url = 'login' 

    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ServiceDeleteView(DeleteView):    
    model = Service
    template_name = 'service_delete.html'
    success_url = reverse_lazy('service_list')
    login_url = 'login' 
    
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ServiceCreateView(LoginRequiredMixin,CreateView):
    model = Service
    template_name = 'service_new.html'
    fields = ('title','schedule','body','cost')
    login_url = 'login' 
    
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

