from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Article
from tag.models import Tag


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class AddingTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','last_login','is_superuser',
                    'username','first_name',
                    'last_name','email',
                    'is_staff','is_active')