from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.db.models import Count
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from .models import Article
from .forms import AddArticleForm, EditArticleForm, AddTag
from .tag import Taggit
from .items import item


# list of articles
# best and last articles
class ArticlesListView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(
            *args, **kwargs)
        # context['best_articles']
        context["last_articles"] = Article.objects.all().order_by(
            "-updated")[:10]
        context["best_article"] = Article.objects.all().order_by(
            "-updated", "-likes_count"
        )[:3]
        return context


# all articles list view
class AllArticleListView(View):

    def get(self, request, *args, **kwargs):
        """
        If the user reaches the bottom of the page, 
        a ajax request will be given to this view 
        and the next five articles will be displayed 
        """
        next_articles = request.GET.get('n')
        # if request not ajax
        if not next_articles:
            articles = Article.objects.all().order_by("-updated")[:10]
            context = {
                'articles': articles
            }
            return render(request, 'blog/article_list.html', context)
        # if send request with ajax
        else:
            next_articles = int(next_articles)
            next_articles += 10
            previous_articles = next_articles - 5
            articles = Article.objects.all().order_by("-updated")[previous_articles:next_articles]
            # create dict for response
            data = item(articles)
            return JsonResponse({'articles': data})


# detail blog
class ArticleDetail(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        article_tags_ids = article.tags.values_list("id", flat=True)
        similar_articles = (
            Article.objects.filter(tags__in=article_tags_ids)
            .exclude(id=article.id)
            .order_by("-updated")
        )
        similar_articles = similar_articles.annotate(same_tags=Count("tags")).order_by(
            "-same_tags", "-updated"
        )[:4]
        context = {"article": article, "similar_articles": similar_articles}
        return render(request, "blog/blog_detail.html", context)


# add article
class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = "user:login"

    def get(self, request, *args, **kwargs):
        context = {"form": AddArticleForm}
        return render(request, "blog/add_article.html", context)

    def post(self, request, *args, **kwargs):
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            article = Article.objects.create(
                title=cd["title"],
                body=cd["body"],
                image=cd["image"],
                user=request.user,
                slug=slugify(cd["title"]),
            )
            tag = Taggit(cd["tags"], article)
            tag.save_object()
            return redirect("/")


# edit article
class EditArticleView(LoginRequiredMixin, View):
    login_url = "user:login"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        form = EditArticleForm(instance=article)
        tag_form = AddTag()
        return render(
            request,
            "blog/article_update_form.html",
            {"form": form, "obj": article, "tag_form": tag_form},
        )

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        form = EditArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            obj = form.save()
            return redirect("/")


# add tag for instance article
class AddNewTag(LoginRequiredMixin, View):
    login_url = "user:login"

    def post(self, request, *args, **kwargs):
        form = AddTag(request.POST)
        if form.is_valid():
            tag = form.save()
            article = get_object_or_404(Article, pk=kwargs["articleId"])
            article.tags.add(tag)
            return redirect(request.META.get("HTTP_REFERER"))


# delete article
class ArticleDeleteView(LoginRequiredMixin, View):
    login_url = "user:login"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        if request.user == article.user:
            return render(
                request, "blog/blog_confirm_delete.html", {"article": article}
            )
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        article.delete()
        return redirect("/")


class SearchArticlesWithTag(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(tags=kwargs["tagid"])
        tag = kwargs["tag"]
        context = {"articles": articles, "tag": tag}
        return render(request, "blog/articles_list.html", context)


# add like view
class AddLikeView(LoginRequiredMixin, View):
    login_url = "user:login"

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        if request.user in article.likes.all():
            # unlike
            article.likes.remove(request.user)
        else:
            # like
            article.likes.add(request.user)
        article.likes_count = article.likes.count()
        article.save()

        return JsonResponse({"likes": article.likes.count()})


# serach view
class SearchView(View):
    def get(self, request, *args, **kwargs):
        query_name = request.GET.get('q')
        if query_name != None and query_name != '':
            articles = Article.objects.filter(title__icontains=query_name)
            articles_by_tag = Article.objects.filter(
                tags__tag__icontains=query_name)
            all_articles = articles | articles_by_tag
            data = item(all_articles)
        return JsonResponse({'articles': data})