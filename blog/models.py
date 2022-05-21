from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from tag.models import TaggedItem


class Article(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    image = models.ImageField(upload_to='blog' , blank=True)
    slug = models.SlugField(null=True , max_length=255)
    tags = GenericRelation(TaggedItem)
    likes = models.ManyToManyField(User , related_name='likes' , blank=True)
    likes_count = models.IntegerField(default=0 , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True , null=True)

    def __str__(self):
        return self.title

