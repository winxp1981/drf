from rest_framework import permissions


class RoomPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
        #   return request.user.is_authenticated() and request.user.is_admin
            print ('allow list @@')
            print ('user: ',request.user)
            return True
        elif view.action in ['create', 'retrieve']:
            print ('user: ',request.user)
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
        #    return request.user.is_authenticated() and (obj == request.user or request.user.is_admin)
            print ('allow retrieve @has_object_permission')
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.is_authenticated() and (obj == request.user or request.user.is_admin)
        elif view.action == 'destroy':
            return request.user.is_authenticated() and request.user.is_admin
        else:
            return False
