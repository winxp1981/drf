from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import ProfileSerializer
from .permissions import UserPermission
from rest_framework.permissions import IsAuthenticated
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

'''
    def get_queryset(self):
        print ("UserViewSet: get_queryset %s" % self.request.user)
        queryset = User.objects.all();
        return queryset
'''
