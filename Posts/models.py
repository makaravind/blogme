from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)
    title = models.CharField(max_length=350)
    content = RichTextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title