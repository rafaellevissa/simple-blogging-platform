from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostDetailSerializer, BlogPostListSerializer, CommentSerializer

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogPostDetailSerializer
        return BlogPostListSerializer

class  BlogPostRetrieveView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(post_id=post_id)
