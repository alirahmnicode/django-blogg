from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class TaggedItem(models.Model):
    tag = models.CharField(max_length=500)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GeneratorExit('content_type' , 'object_id')

    def __str__(self):
        return self.tag
