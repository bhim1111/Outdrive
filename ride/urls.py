
from django.urls import path

from .views import AcceptRideView, HomeView, RideDeleteView, RideListView, RideUpdateView, RideCreateView, CompleteRideView, RideSearchView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('ride_create/', RideCreateView.as_view(), name='ride_create'),
    path('ride_list/', RideListView.as_view(), name='ride_list'),
    
    path('ride_update/<int:pk>/', RideUpdateView.as_view(), name='ride_update'),
    path('ride_delete/<int:pk>/', RideDeleteView.as_view(), name='ride_delete'),
    path('ride_accept/<int:pk>/', AcceptRideView.as_view(), name='ride_accept'),
    path("ride/complete/<int:ride_id>/", CompleteRideView.as_view(), name="complete_ride"), 
    path('search/', RideSearchView.as_view(), name='search'), 
    
]
