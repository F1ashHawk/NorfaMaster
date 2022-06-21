from django.urls import path

from .views import BidListView,BidDetailView,BidCreateView

urlpatterns = [
   
    path('<int:pk>/',BidDetailView.as_view(), name='bid_detail'), 
    path('new/', BidCreateView.as_view(), name='bid_new'), 
    path('', BidListView.as_view(), name='bid_list'),
]
