from django.urls import path

from .views import ServicesListView,ServiceUpdateView,ServiceDetailView,ServiceDeleteView,ServiceCreateView

urlpatterns = [
    path('<int:pk>/edit/',ServiceUpdateView.as_view(), name='service_edit'), 
    path('<int:pk>/',ServiceDetailView.as_view(), name='service_detail'), 
    path('<int:pk>/delete/',ServiceDeleteView.as_view(), name='service_delete'), 
    path('new/', ServiceCreateView.as_view(), name='service_new'), 
    path('', ServicesListView.as_view(), name='services_list'),
]
