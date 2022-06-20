from django.urls import path

from .views import WorkerListView,WorkerUpdateView,WorkerDetailView,WorkerDeleteView,WorkerCreateView

urlpatterns = [
    path('<int:pk>/edit/',WorkerUpdateView.as_view(), name='worker_edit'), 
    path('<int:pk>/',WorkerDetailView.as_view(), name='worker_detail'), 
    path('<int:pk>/delete/',WorkerDeleteView.as_view(), name='worker_delete'), 
    path('new/', WorkerCreateView.as_view(), name='worker_new'), 
    path('', WorkerListView.as_view(), name='worker_list'),
]
