from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from .models import CustomUser

class MakeCustomUser(UserCreationForm):
    password1 = forms.CharField(label="Wachtwoord", strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),)
    password2 = forms.CharField(label="Herhaal wachtwoord", widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), strip=False,)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
        help_texts = {'username': None}
        labels = {'username': 'Gebruikersnaam', 'email': 'E-mailadres', 'first_name': 'Voornaam', 'last_name': 'Achternaam'}

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(label="Gebruikersnaam", widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Wachtwoord", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),)