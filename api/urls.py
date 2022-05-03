from django.urls import path 
from .views import ArticleList , ArticleDetails


app_name = 'api'

urlpatterns = [
    path('all-article/' , ArticleList.as_view()),
    path('article/detail/<int:pk>/' , ArticleDetails.as_view()),
]