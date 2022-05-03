from .models import Tag


class Taggit:
    def __init__(self, tags, obj):
        self.tags = tags
        self.obj = obj

    def split_tag(self):
        return self.tags.split(",")

    def save_object(self):
        for tag in self.split_tag():
            try:
                r_tag = Tag.objects.get(tag=tag)
                print(r_tag)
                self.obj.tags.add(tag)
                print(tag)
            except:
                print("ali")
                tag = Tag.objects.create(tag=tag)
                self.obj.tags.add(tag)
