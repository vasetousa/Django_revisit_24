from django.contrib.auth.views import LogoutView
from django.urls import path

from UserApp.userRegister.views import HomeView, UserRegisterView, UserLoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]