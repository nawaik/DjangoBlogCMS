from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from .forms import MakeCustomUserForm, CustomAuthenticationForm, ProfileForm
from .models import CustomUser

class CustomUserCreationView(CreateView):
    form_class = MakeCustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    success_url = '/profiel/'
    template_name = 'gebruiker/profiel.html'

    def get_queryset(self):
        return CustomUser.objects.get(username=self.request.user)

    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.request.user.id)