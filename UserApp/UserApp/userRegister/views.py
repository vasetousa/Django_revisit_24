from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, authenticate, login, get_user_model

from UserApp.userRegister.forms import UserRegistrationForm

UserModel = get_user_model()


# Create your views here.

class HomeView(views.TemplateView):
    template_name = 'home.html'


class UserRegisterView(views.CreateView):
    model = UserModel
    form_class = UserRegistrationForm  # our own creation form is used
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        # Save the form data
        response = super().form_valid(form)

        # Log in the user after registration
        username = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(self.request, user)

        return response


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return reverse_lazy('home')
