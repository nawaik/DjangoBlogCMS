from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import CustomUserCreationView, CustomLoginView, ProfileUpdateView, ProfileDetailView

urlpatterns = [
    path('registreren/', CustomUserCreationView.as_view(), name="register"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profielbewerken/', ProfileUpdateView.as_view(), name="profielbewerken"),
    path('profiel/<int:pk>/', ProfileDetailView.as_view(), name="profiel"),
]
