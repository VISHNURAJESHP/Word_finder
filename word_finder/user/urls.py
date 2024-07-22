from django.urls import path
from .views import UserRegistrationView , LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login-view'),
    path('userregister', UserRegistrationView.as_view(), name='user-register'),
]