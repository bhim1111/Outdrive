from django.contrib import admin
from .models import Driver, Ride

# Register your models here.

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'licence_number', 'vehicle_type', 'vehicle_number', 'is_available')
    search_fields = ('user__username', 'licence_number', 'vehicle_number')
    list_filter = ('vehicle_type', 'is_available')
    
@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('user', 'driver', 'pickup_location', 'dropoff_location', 'fare', 'status', 'created_at')
    search_fields = ('user__username', 'driver__user__username', 'pickup_location', 'dropoff_location')
    list_filter = ('status', 'created_at')