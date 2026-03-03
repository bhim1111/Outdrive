
from django.urls import path

from .views import HomeView, RideDeleteView, RideListView, RideUpdateView, RideCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('ride_create/', RideCreateView.as_view(), name='ride_create'),
    path('ride_list/', RideListView.as_view(), name='ride_list'),
    
    path('ride_update/<int:pk>/', RideUpdateView.as_view(), name='ride_update'),
    path('ride_delete/<int:pk>/', RideDeleteView.as_view(), name='ride_delete'),
   
]
