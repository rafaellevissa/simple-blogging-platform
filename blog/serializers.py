from rest_framework import serializers
from .models import BlogPost, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at']
        read_only_fields = ['id', 'created_at', 'post']


class BlogPostListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comment_count']

class BlogPostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'comments']
