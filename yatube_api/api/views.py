from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)

from posts.models import Group, Follow, Post, User
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (
    CommentSerializer, GroupSerializer,
    PostSerializer, FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly, IsAuthorOrReadOnlyPermission
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                    ):
    """Вюсет подписок."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет комментариев к постам."""
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly, IsAuthorOrReadOnlyPermission
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
