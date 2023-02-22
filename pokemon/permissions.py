from rest_framework import permissions


class ObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if view.action == "list":
            return True
        return obj.trainer == request.user
