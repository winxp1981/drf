from rest_framework import permissions

# 只允許查看 (GET) 自己的 id
# http://localhost:8000/user/1/   要附token
class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'retrieve':
        #    print ('user: ',request.user)
            return request.user.is_authenticated()
        else:
            return False

    def has_object_permission(self, request, view, obj):
        print ("UserPermission: has_object_permission: ", view.action)
        if view.action == 'retrieve':
        #    return request.user.is_authenticated() and (obj == request.user or request.user.is_staff)
            return request.user.is_authenticated() and (obj == request.user)
        else:
            return False
