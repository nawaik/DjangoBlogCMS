from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Articles

class ShowArticles(ListView):
    model = Articles
    paginate_by = 40
    template_name = 'home.html'
