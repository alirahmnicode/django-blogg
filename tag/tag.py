from .models import TaggedItem , Tag


class Taggit:
    def __init__(self, tags, obj):
        self.tags = tags
        self.obj = obj
        self.split_tags = None

    def split_tag(self):
        self.split_tags = self.tags.split(',')
        
    def save_object(self):
        self.split_tag()
        for tag in self.split_tags:
            tag = Tag.objects.get_or_create(label=tag)
            tag_item = TaggedItem(content_object=self.obj,tag=tag[0])
            tag_item.save()