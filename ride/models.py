from django.db import models

from django.contrib.auth.models import User
#Driver model
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    licence_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
        
    
    
#Ride model
class Ride(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    
    fare = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ride {self.id} - {self.user.username} to {self.dropoff_location}"
    




class Profile(models.Model):
    
    PROFILE_CHOICES = [
        ('passenger', 'Passenger'),
        ('driver', 'Driver'),
    ]
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=PROFILE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
