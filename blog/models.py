from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify



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
    tags = TaggableManager()
    likes = models.ManyToManyField(User , related_name='likes' , blank=True)
    likes_count = models.IntegerField(default=0 , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True , null=True)

    objects = ArticleManager()

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_similar_articles(self):
        article_tags = self.tags.values_list("id", flat=True)
        similar_articles = (
            Article.objects.filter(tags__in=article_tags)
            .exclude(id=self.id)
        )
        similar_articles = similar_articles.annotate(same_tags=Count("tags")).order_by(
            "-same_tags", "-updated"
        )[:4]
        return similar_articles

    def like(self, request):
        if request.user in self.likes.all():
            # unlike
            self.likes.remove(request.user)
        else:
            # like
            self.likes.add(request.user)
        self.likes_count = self.likes.count()
        self.save()
        return self.likes_count

    def __str__(self):
        return self.title

