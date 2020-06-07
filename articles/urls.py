from django.urls import path

from .views import (
    ShowArticlesView,
    CreateArticleView,
    DetailArticleView,
    ShowOwnArticlesView,
    UpdateArticleView,
    DeleteArticleView,
    ShowProfileArticlesView,
    ShowArticleCommentsView,
    CreateCommentView,
    UpdateCommentView,
    DeleteCommentView,
)

urlpatterns = [
    path('', ShowArticlesView.as_view(), name='homepage'),
    path('artikels', ShowOwnArticlesView.as_view(), name="artikels"),
    path('comments', ShowArticleCommentsView.as_view(), name="comments"),
    path('artikel/<int:pk>', DetailArticleView.as_view(), name="artikeldetail"),
    path('artikelaanmaken/', CreateArticleView.as_view(), name='artikelaanmaken'),
    path('commentaanmaken/<int:pk>', CreateCommentView.as_view(), name='commentaanmaken'),
    path('artikel/bewerken/<int:pk>', UpdateArticleView.as_view(), name="artikelbewerken"),
    path('comment/bewerken/<int:pk>', UpdateCommentView.as_view(), name="commentbewerken"),
    path('artikel/verwijder/<int:pk>', DeleteArticleView.as_view(), name="artikelverwijderen"),
    path('comment/verwijder/<int:pk>', DeleteCommentView.as_view(), name="commentverwijderen"),
    path('profiel/<int:author_id>/artikels', ShowProfileArticlesView.as_view(), name="profielartikels"),
]