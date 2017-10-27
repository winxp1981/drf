from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .serializers import UserSerializer
from .serializers import ProfileSerializer
from .permissions import UserPermission
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile

'''
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
#    permission_classes = (UserPermission,)
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    # 更新 user profile (只更新 body 裡有的欄位)
    # e.g. POST  http://localhost:8000/user/1/edit_profile/
    '''
    body:
    {
        "nick_name": "",
        "mobile_no": "0922888888",
        "birth_date": "1981-04-06",
        "avatar_url": "http://www.gravatar.com/avatar?d=mm"
    }
    '''
    @detail_route(methods=['post'])
    def edit_profile(self, request, pk=None):
        print ("update profile %s (%s)" % (request.user, pk) )
    #    print (request.data)
        _profile = Profile.objects.get(user_id=pk)
        _fields_to_update = []

        for attr, value in request.data.items():
            print ("%s: %s" % (attr, value) )
            setattr(_profile, attr, value)
            _fields_to_update.append(attr)

        print (_fields_to_update)
        _profile.save(update_fields=_fields_to_update)
        # getattr(_profile, 'mobile_no')
        # setattr(_profile, 'mobile_no', '0922xxxxxx')
    #    room.who_likes.add(request.user)
    #    print (Room.objects.get(id=pk).who_likes.count())
        return Response(status=status.HTTP_200_OK)
