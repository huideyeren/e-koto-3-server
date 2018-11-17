from rest_framework import serializers
from diary.models import Post

class PostSerialize(serializers.ModelSerializer):
    """記事のシリアライザ"""
    class Meta:
        model = Post
        fields = '__all__'