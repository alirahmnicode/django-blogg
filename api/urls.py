from django.urls import path 
from .views import (ArticleList ,
                    ArticleDetails ,
                    ArticleCreateView ,
                    ArticleUpdateView ,
                    ArticleDeleteView,
                    AddingTagView,
                    AddingLikeView,
                    FilterByTag)


app_name = 'api'

urlpatterns = [
    path('all-article/' , ArticleList.as_view()),
    path('article/detail/<int:pk>/' , ArticleDetails.as_view()),
    path('article/create/' , ArticleCreateView.as_view()),
    path('article/update/<int:pk>/' , ArticleUpdateView.as_view()),
    path('article/delete/<int:pk>/' , ArticleDeleteView.as_view()),
    path('article/create-tag/' , AddingTagView.as_view()),
    path('article/add-like/<int:pk>/' , AddingLikeView.as_view()),
    path('articles/tag/<str:tag>/' , FilterByTag.as_view()),
]