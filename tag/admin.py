from django.contrib import admin
from .models import TaggedItem , Tag


admin.site.register(TaggedItem)
admin.site.register(Tag)