from rest_framework import permissions

# authentication: 有沒有
# authorization: 能不能

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
        elif view.action in ['update', 'partial_update']:
            return False
        elif view.action in['like', 'dislike']:   # 自定
            print ('user: ',request.user)
            print ('authenticated: ',request.user.is_authenticated())
            return request.user.is_authenticated()
        elif view.action in ['destroy']:
            print ('has permission to destroy: %d' % (request.user.is_authenticated() and request.user.is_staff))
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        print ("has_object_permission: ", view.action)
        if view.action == 'retrieve':
        #    return request.user.is_authenticated() and (obj == request.user or request.user.is_admin)
        #    print ('allow retrieve @has_object_permission')
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.is_authenticated() and (obj == request.user or request.user.is_staff)
        elif view.action == 'destroy':
            return request.user.is_authenticated() and request.user.is_staff
        else:
            return False
