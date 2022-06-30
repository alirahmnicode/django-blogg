from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Article
from .forms import ArticleForm
from .listing_obj import Listing


# list of articles
# best and last articles
class ArticlesListView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(
            *args, **kwargs)
        context["last_articles"] = Article.objects.last_articles()
        context["best_article"] = Article.objects.best_aricles()
        return context


# all articles list view
class AllArticleListView(View):

    def get(self, request, *args, **kwargs):
        """
        If the user reaches the bottom of the page, 
        a ajax request will be given to this view 
        and the next 10 articles will be displayed 
        """
        end_articles = request.GET.get('n')
        # if request not ajax
        if not end_articles:
            articles = Article.objects.last_articles()
            context = {
                'articles': articles
            }
            return render(request, 'blog/article_list.html', context)
        # if send request with ajax
        else:
            objs = Article.objects.all()
            listing = Listing(objs=objs)
            listing.range_of_objects(10, end_articles)
            data = listing.get_objects()
            return JsonResponse({'articles': data})


# detail blog
class ArticleDetail(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        similar_articles = article.get_similar_articles()
        context = {"article": article, 'similar_articles':similar_articles}
        return render(request, "blog/blog_detail.html", context)


# add article
class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = "user:login"

    def get(self, request, *args, **kwargs):
        context = {"form": ArticleForm}
        return render(request, "blog/add_article.html", context)

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)            
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return redirect("/")


# edit article
class EditArticleView(LoginRequiredMixin, View):
    login_url = "user:login"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        form = ArticleForm(instance=article)
        context = {"form": form, "obj": article}
        return render(
            request,
            "blog/article_update_form.html",
            context
        )

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            obj = form.save()
            return redirect("/")



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


class FilterByTag(View):
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
            listing = Listing()
            data = listing.list_objects(articles)
        return JsonResponse({'articles': data})
