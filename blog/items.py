def item(obj):
    data = []
    if obj:
        for article in obj:
            item = {
                "pk": article.pk,
                "title": article.title,
                "body": article.body,
                "user": article.user.username,
                "image": article.image.url,
                "slug": article.slug,
                "tags": [tag.tag for tag in article.tags.all()],
            }
            data.append(item)
    return data
