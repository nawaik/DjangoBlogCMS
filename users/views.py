from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import MakeCustomUser

class CustomUserCreation(CreateView):
    form_class = MakeCustomUser
    success_url = 'login'
    template_name = 'registration/registration.html'