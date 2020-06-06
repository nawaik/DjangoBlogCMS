from django.urls import path

from .views import ShowArticles

urlpatterns = [
    path('', ShowArticles.as_view(), name='homepage'),
]
