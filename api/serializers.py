from dataclasses import fields
from rest_framework import serializers
from blog.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class AddingTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'