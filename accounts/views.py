from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm

# Create your views here.

class UserLoginView(LoginView):
    # use the app's login template under register/ (ride and accounts apps share similar structures)
    template_name = 'register/login.html'
    # attach our custom form styling
    authentication_form = LoginForm
    # if a logged-in user hits the login page, send them home
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')







