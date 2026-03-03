from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ride
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView



# Create your views here.

class HomeView(TemplateView):
   template_name = 'home.html'
   def get(self,request):
         rides = Ride.objects.all()
         return render(request, self.template_name, {'rides': rides})
   

        
class RideListView(LoginRequiredMixin, ListView):
    model = Ride
    template_name = 'ride_list.html'
    context_object_name = 'rides'

    def get_queryset(self):
        return Ride.objects.filter(user=self.request.user)
    
    
    
class RideCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    fields = ['pickup_location', 'dropoff_location', 'fare']
    template_name = 'ride_create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    


class RideUpdateView(LoginRequiredMixin, UpdateView):
    model = Ride
    fields = ['pickup_location', 'dropoff_location', 'fare']
    template_name = 'ride_update.html'
    success_url = reverse_lazy('home')
    
    def get_query(self):
        return Ride.objects.filter(user=self.request.user)
    
    
class RideDeleteView(LoginRequiredMixin, DeleteView):
    model =Ride
    template_name = 'ride_delete.html'
    success_url = reverse_lazy('home')
    

