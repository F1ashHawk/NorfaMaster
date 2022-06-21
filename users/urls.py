from django.urls import path

from .views import ClientSignUpView,CompanySignUpView

urlpatterns = [
    path('client_signup/', ClientSignUpView.as_view(), name='client_signup'),
    path('company_signup/', CompanySignUpView.as_view(), name='company_signup'),
]
