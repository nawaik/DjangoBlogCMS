from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from .forms import CreateArticleForm
from .models import Articles

class ShowArticlesView(ListView):
    model = Articles
    paginate_by = 40
    template_name = 'home.html'

class DetailArticleView(DetailView):
    model = Articles
    template_name = 'artikelen/articledetail.html'

class ShowOwnArticlesView(ListView):
    model = Articles
    paginate_by = 40
    template_name = 'artikelen/articlelist.html'

    def get_queryset(self):
        return Articles.objects.filter(author=self.request.user)

class ShowProfileArticlesView(ListView):
    model = Articles
    paginate_by = 40
    template_name = 'artikelen/userarticle.html'

    def get_queryset(self):
        return Articles.objects.filter(author_id=self.kwargs['author_id'])

class CreateArticleView(CreateView):
    form_class = CreateArticleForm
    template_name = 'artikelen/createarticle.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateArticleView(UpdateView):
    model = Articles
    fields = ['title', 'text', 'meta_title', 'meta_description']
    template_name = 'artikelen/updatearticle.html'

class DeleteArticleView(DeleteView):
    model = Articles
    context_object_name = 'article'
    success_url = reverse_lazy('artikels')
    template_name = 'artikelen/deletearticle.html'