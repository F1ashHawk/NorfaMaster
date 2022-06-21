from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from users.views import ClientSignUpView,CompanySignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')), 
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('client_signup/', ClientSignUpView.as_view(), name='signup'),
    path('company_signup/', CompanySignUpView.as_view(), name='company_signup'),
    path('services/', include('services.urls')), 
    path('workers/', include('workers.urls')), 
    path('bids/', include('bids.urls')), 
]