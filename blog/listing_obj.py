class Listing:
    def __init__(self, objs=None) -> None:
        self.objs = objs

    def range_of_objects(self, number_of_objects, end_articles):
        self.next_articles = int(end_articles)
        self.previous_articles = end_articles - number_of_objects

    def get_objects(self):
        if self.objs:
            objects = self.objs[self.previous_articles:self.next_articles]
            return self.list_objects(objects)

    def list_objects(self, objects):
        data = []
        if objects:
            for obj in objects:
                item = {
                    "pk": obj.pk,
                    "title": obj.title,
                    "body": obj.body,
                    "user": obj.user.username,
                    "image": obj.image.url,
                    "slug": obj.slug,
                    "tags": [tag.name for tag in obj.tags.all()],
                }
                data.append(item)
        return data
