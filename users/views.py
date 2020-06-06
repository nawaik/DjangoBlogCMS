from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from .forms import MakeCustomUser, CustomAuthenticationForm

class CustomUserCreationView(CreateView):
    form_class = MakeCustomUser
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'