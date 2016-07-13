from rest_framework import serializers
from .models import Post

class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'timestamp', 'updated']

