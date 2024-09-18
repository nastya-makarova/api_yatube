from rest_framework import serializers

from posts.models import Comment, Group, Post, User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'posts')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('author', 'post', 'created', 'text')


class PostSerializer(serializers.ModelSerializer):
    # group = serializers.SlugRelatedField(
    #     slug_field='slug',
    #     queryset=Group.objects.all(),
    #     required=False
    # )
    comments = CommentSerializer(many=True, required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('text', 'author', 'pub_date', 'image', 'group', 'comments')
