from django.urls import path
from .views import BlogPostListCreateView, BlogPostRetrieveView, CommentCreateView

urlpatterns = [
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostRetrieveView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
]
