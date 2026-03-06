from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm





class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=150, required=True, 
                             widget=forms.TextInput(
                                 attrs={"class": "form-control", "placeholder": "Username"}))
    
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}))
    
    
    
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password1 = forms.CharField(label="Password", required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(label="Confirm Password", required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}))