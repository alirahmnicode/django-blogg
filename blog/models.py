from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from tag.models import TaggedItem



class ArticleManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().all().order_by("-updated")

    def last_articles(self):
        return self.get_queryset()[:10]

    def best_aricles(self):
        return self.get_queryset().all().order_by("-likes_count")[:3]


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

    objects = ArticleManager()

    def __str__(self):
        return self.title

