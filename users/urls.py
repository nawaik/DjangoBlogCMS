from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import CustomUserCreationView, CustomLoginView

urlpatterns = [
    path('gebruiker/register/', CustomUserCreationView.as_view(), name="register"),
    path('gebruiker/login/', CustomLoginView.as_view(), name="login"),
    path('gebruiker/logout/', LogoutView.as_view(), name="logout"),
]
