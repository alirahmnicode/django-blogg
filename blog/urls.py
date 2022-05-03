from django.urls import path
from . import views


app_name = 'article'

urlpatterns = [
    path('' , views.ArticlesListView.as_view() , name="index"),
    path('articles/all/' , views.AllArticleListView.as_view() , name="all"),
    path('articles/detail/<slug:slug>/<int:pk>/' , views.ArticleDetail.as_view() , name="detail"),
    path('articles/add-article/' , views.ArticleCreateView.as_view() , name="add"),
    path('articles/edit-article/<int:pk>/' , views.EditArticleView.as_view() , name="edit"),
    path('articles/delete-article/<int:pk>/' , views.ArticleDeleteView.as_view() , name="delete"),
    path('articles/list/<str:tag>/<int:tagid>/' , views.SearchArticlesWithTag.as_view() , name="tag"),
    path('articles/add-new-tag/<int:articleId>/' , views.AddNewTag.as_view() , name="addtag"),
    path('articles/like/<int:pk>/' , views.AddLikeView.as_view() , name="like"),
    path('blog/search/' , views.SearchView.as_view() , name="search"),
]