from rest_framework import viewsets
from .models import Room
from .models import RoomImage
from .serializers import RoomSerializer
from .serializers import RoomImageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import RoomPermission


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    #permission_classes = (StorePermission,)
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    # filter_fields = ('number', 'address')
    search_fields = ('location', 'description')  # example POST: http://localhost:8000/stores/?search=ab0

"""
    def retrieve(self, request, pk=None):
        print ('!! has_object_permission')
        print ('@@ store retrieve: ' + pk)
"""


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer
