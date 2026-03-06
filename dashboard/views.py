from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ride.models import Ride
# Create your views here.




class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
  

    def get(self, request, *args, **kwargs):
        user = request.user
        
        total_rides = Ride.objects.filter(user=user).count()
        pending_rides = Ride.objects.filter(user=user, status='pending').count()
        accepted_rides = Ride.objects.filter(user=user, status='accepted').count()
        completed_rides = Ride.objects.filter(user=user, status='completed').count()
        
        context = {
            'total_rides': total_rides,
            'pending_rides': pending_rides,
            'accepted_rides': accepted_rides,
            'completed_rides': completed_rides,
        }
        
        
        return render(request, self.template_name, context)
        