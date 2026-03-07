from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Driver, Ride
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView, View
from django.db.models import Q



# Create your views here.

class HomeView(TemplateView):
   template_name = 'home.html'
   def get(self,request):
         rides = Ride.objects.all( )
         return render(request, self.template_name, {'rides': rides})
   

        
class RideListView(LoginRequiredMixin, ListView):
    model = Ride
    template_name = 'ride_list.html'
    context_object_name = 'rides'
    
    
    def get_queryset(self):
        return Ride.objects.filter(status = "pending")
            
            
           
            
            
class AcceptRideView(View):
    model = Ride
    fields = []
    
    def get(self, request, *args, **kwargs):
        ride = Ride.objects.get(pk=kwargs['pk'])
        driver = Driver.objects.filter(user=request.user).first()
        if not driver:
         return HttpResponse("Only drivers can accept rides")
        ride.driver = driver
        ride.status = 'accepted'
        ride.save()
        return redirect("ride_list")
    
    
   
    
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
    



class CompleteRideView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = Ride.objects.filter(id=ride_id).first()
        if ride.driver and ride.driver.user == request.user:
            ride.status = "completed"
            ride.save()
            return redirect('dashboard')
        else:
            return HttpResponse("Only the assigned driver can complete this ride.")
        
        
        
        
        
        


class RideSearchView(LoginRequiredMixin, ListView):
    model = Ride
    template_name = 'ride_search.html'
    context_object_name = 'rides'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            return Ride.objects.filter(
                Q(pickup_location__icontains=query) |
                Q(dropoff_location__icontains=query)
            )

        return Ride.objects.all()
