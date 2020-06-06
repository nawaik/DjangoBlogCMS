from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MakeCustomUserForm, CustomAuthenticationForm, ProfileForm
from .models import CustomUser

class CustomUserCreationView(CreateView):
    form_class = MakeCustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    success_url = '/profiel/'
    template_name = 'gebruiker/profielupdaten.html'

    def get_queryset(self):
        return CustomUser.objects.get(username=self.request.user)

    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.request.user.id)

class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'gebruiker/profiel.html'