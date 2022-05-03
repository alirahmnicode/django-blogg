from django.urls import path 
from .views import (ArticleList ,
                     ArticleDetails ,
                     ArticleCreateView ,
                     ArticleUpdateView ,
                     ArticleDeleteView)


app_name = 'api'

urlpatterns = [
    path('all-article/' , ArticleList.as_view()),
    path('article/detail/<int:pk>/' , ArticleDetails.as_view()),
    path('article/create/' , ArticleCreateView.as_view()),
    path('article/update/<int:pk>/' , ArticleUpdateView.as_view()),
    path('article/delete/<int:pk>/' , ArticleDeleteView.as_view()),
]