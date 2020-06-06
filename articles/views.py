from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .forms import CreateArticleForm
from .models import Articles

class ShowArticlesView(ListView):
    model = Articles
    paginate_by = 40
    template_name = 'home.html'

class DetailArticleView(DetailView):
    model = Articles
    template_name = 'artikelen/articledetail.html'

class CreateArticleView(CreateView):
    form_class = CreateArticleForm
    template_name = 'artikelen/createarticle.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

