from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.instance

        if instance.author != self.request.user:
            raise PermissionDenied

        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_post(self):
        post_id = self.kwargs['post_id']
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def perform_update(self, serializer):
        instance = serializer.instance

        if instance.author != self.request.user:
            raise PermissionDenied

        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
