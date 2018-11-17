from django.http import HttpResponse
from rest_framework import viewsets
from diary.models import Post
from diary.serializers import PostSerialize

class PostViewSets(viewsets.ModelViewSet):
    """投稿の記事"""

    queryset = Post.objects.all()
    serializer_class = PostSerialize