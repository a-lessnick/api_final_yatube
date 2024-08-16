from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Класс контроля прав доступа к объектам."""

    def has_object_permission(self, request, views, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
