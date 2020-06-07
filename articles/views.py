from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from .forms import CreateArticleForm, CreateCommentsForm
from .models import Articles

class ShowArticlesView(ListView):
    model = Articles
    paginate_by = 40
    template_name = 'home.html'

class DetailArticleView(DetailView):
    model = Articles
    template_name = 'artikelen/articledetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateCommentsForm
        return context

class ShowOwnArticlesView(LoginRequiredMixin, ListView):
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

class CreateArticleView(LoginRequiredMixin, CreateView):
    form_class = CreateArticleForm
    template_name = 'artikelen/createarticle.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateArticleView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ['title', 'text', 'meta_title', 'meta_description']
    template_name = 'artikelen/updatearticle.html'

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser or self.request.user.is_staff:
            return obj.author == obj.author
        else:
            return obj.author == self.request.user


class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    context_object_name = 'article'
    success_url = reverse_lazy('artikels')
    template_name = 'artikelen/deletearticle.html'

    def test_func(self):
        obj = self.get_object()
        if self.request.user.is_superuser or self.request.user.is_staff:
            return obj.author == obj.author
        else:
            return obj.author == self.request.user