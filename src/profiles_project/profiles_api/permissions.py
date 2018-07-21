from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

class PostOwnMessage(permissions.BasePermission):
    """Allow users to update their own message."""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id 

class PostOwnPost(permissions.BasePermission):
    """Allow users to update their own posts"""

    def has_object_permission(self, request, view, obj):
        """Checks if the user is updating their own post."""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.poster.id == request.user.id

class LikeOwnPost(permissions.BasePermission):
    """Allow users to update their own likes"""

    def has_object_permission(self, request, view, obj):
        """Checks if the user is trying to change their own like"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user.id == request.user.id
