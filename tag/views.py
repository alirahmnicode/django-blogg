from django.shortcuts import render , redirect
from .models import TaggedItem
from .tag import Taggit
from blog.models import Article

 
def delete_tag(request , obj_id , tag_id):
    tagged_item = TaggedItem.objects.get(object_id=obj_id , tag=tag_id)
    if tagged_item:
        tagged_item.delete()
    return redirect(request.META.get("HTTP_REFERER"))


def add_new_tag(request, obj_id):
    obj = Article.objects.get(pk=obj_id)
    tags = request.POST.get('label')
    tag = Taggit(tags,obj)
    tag.save_object()
    return redirect(request.META.get("HTTP_REFERER"))
