from django.urls import path 
from .views import ArticleList


app_name = 'api'

urlpatterns = [
    path('all-article/' , ArticleList.as_view()),
]