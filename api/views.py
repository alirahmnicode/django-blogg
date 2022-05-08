from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied

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
        data = dict(serializer.validated_data)
        user = self.request.user
        slug = slugify(data['title'])
        if user:
            serializer.save(user=user,slug=slug)
        else:
            return Response('User not found ...',status=204)

class ArticleUpdateView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        obj = self.get_object()
        if self.request.user != obj.user:
            raise PermissionDenied()
        serializer.save()

class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        obj = self.get_object()

        if self.request.user != obj.user:
            raise PermissionDenied()
        instance.delete()


class AddingTagView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = AddingTagSerializer
    permission_classes = [IsAuthenticated]


class AddingLikeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,**kwargs):
        user = request.user
        if user:
            article = get_object_or_404(Article , pk=kwargs['pk'])
            if user in article.likes.all():
                article.likes.remove(user)
                message = 'unliked'
            else:
                article.likes.add(user)
                message = 'liked'
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
