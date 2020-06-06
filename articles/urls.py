from django.urls import path

from .views import ShowArticlesView, CreateArticleView, DetailArticleView, ShowOwnArticlesView, UpdateArticleView, DeleteArticleView, ShowProfileArticlesView

urlpatterns = [
    path('', ShowArticlesView.as_view(), name='homepage'),
    path('artikels', ShowOwnArticlesView.as_view(), name="artikels"),
    path('artikel/<int:pk>', DetailArticleView.as_view(), name="artikeldetail"),
    path('artikelaanmaken/', CreateArticleView.as_view(), name='artikelaanmaken'),
    path('artikel/bewerken/<int:pk>', UpdateArticleView.as_view(), name="artikelbewerken"),
    path('artikel/verwijder/<int:pk>', DeleteArticleView.as_view(), name="artikelverwijderen"),
    path('profiel/<int:author_id>/artikels', ShowProfileArticlesView.as_view(), name="profielartikels"),
]
