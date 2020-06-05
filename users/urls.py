from django.urls import path, include

from .views import CustomUserCreation

urlpatterns = [
    path('gebruiker/register', CustomUserCreation.as_view(), name="register"),
    path('gebruiker/', include('django.contrib.auth.urls')),
]
