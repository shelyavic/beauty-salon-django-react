from salon_api.utils import has_group
from rest_framework import permissions
from django.conf import settings

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.client == request.user


class IsMaster(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return has_group(request.user, settings.MASTER_GROUP_NAME)


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return view.kwargs["pk"] == request.user.id
