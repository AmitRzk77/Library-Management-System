from rest_framework.permissions import BasePermission, IsAuthenticated

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsAdminLevel(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class bookPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in["List"]:
            return True
        elif view.action in ["retrive"]:
            return isOwner(request)
        elif view.action in ['create', 'update']:
            return IsAuthenticated(request)
        elif view.action == 'partial_update':
            return IsAuthenticated(request)
        elif view.action == "destroy":
            return AdminLevel(request)

        