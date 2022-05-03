from rest_framework import generics
from .serializers import ArticleSerializer

from blog.models import Article


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
