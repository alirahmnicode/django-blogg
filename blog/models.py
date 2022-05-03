from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    image = models.ImageField(upload_to='blog' , blank=True)
    slug = models.SlugField(null=True , max_length=255)
    tags = models.ManyToManyField('Tag' , related_name='tags' , blank=True)
    likes = models.ManyToManyField(User , related_name='likes' , blank=True)
    likes_count = models.IntegerField(default=0 , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True , null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.tag}'
