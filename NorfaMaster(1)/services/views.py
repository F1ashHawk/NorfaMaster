from django.views.generic import ListView

from .models import Service

class ServicesListView(ListView):
    model = Service
    template_name = 'services_list.html'