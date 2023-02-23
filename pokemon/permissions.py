from rest_framework import permissions


class ObjectPermission(permissions.BasePermission):
    message = "this pokemon is not yours, mind your business"

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if view.action == "list" or obj.trainer == request.user:
            return True
        return False
