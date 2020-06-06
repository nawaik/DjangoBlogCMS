from django.urls import path

from .views import ShowArticlesView, CreateArticleView, DetailArticleView

urlpatterns = [
    path('', ShowArticlesView.as_view(), name='homepage'),
    path('artikel/<int:pk>', DetailArticleView.as_view(), name="artikeldetail"),
    path('artikelaanmaken/', CreateArticleView.as_view(), name='artikelaanmaken'),
]
