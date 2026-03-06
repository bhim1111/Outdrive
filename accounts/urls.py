
from django import views
from django.urls import path
from accounts import views



from django.contrib.auth import views as auth_views
from .views import UserLoginView

urlpatterns = [
  
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]