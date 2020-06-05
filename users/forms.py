from django.forms import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class MakeCustomUser(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')