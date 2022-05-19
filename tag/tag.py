from .models import TaggedItem


class Taggit:
    def __init__(self, tags, obj):
        self.tags = tags
        self.obj = obj

    def split_tag(self):
        return self.tags.split(",")

    def save_object(self):
        for tag in self.split_tag():
            try:
                r_tag = TaggedItem.objects.get(tag=tag)
                self.obj.tags.add(tag)
            except:
                tag = TaggedItem.objects.create(tag=tag)
                self.obj.tags.add(tag)