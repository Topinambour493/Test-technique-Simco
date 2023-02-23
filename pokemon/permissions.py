from rest_framework import permissions


class ObjectPermission(permissions.BasePermission):
    message = "this pokemon is not yours, mind your business"

    def has_object_permission(self, request, view, obj):
        if view.action == "list" or obj.trainer == request.user:
            return True
        return False
