from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from .serializers import ArticleSerializer , AddingTagSerializer ,UserSerializer

from blog.models import Article, Tag


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    

class ArticleDetails(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save(user=self.request.user)

class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AddingTagView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = AddingTagSerializer
    permission_classes = [IsAuthenticated]


class AddingLikeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,**kwargs):
        user = request.user.id
        if user:
            article_pk = kwargs['pk']
            article = get_object_or_404(Article , pk=article_pk)
            if user not in article.likes.all():
                article.likes.add(user)
                message = 'liked'
            else:
                article.likes.remove(user)
                message = 'unliked'
            article.save()
            
            return Response(message,status=200)
        else:
            return Response('user not found...' , status=404)


class FilterByTag(APIView):
    def get(self,request,**kwargs):
        tag = kwargs['tag']
        articles = Article.objects.filter(tags__tag__icontains=tag)
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data,status=200)



class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
