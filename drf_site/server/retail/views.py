from rest_framework import viewsets
from retail.models import Chain, Store, Employee, RoomInfo
from retail.serializers import ChainSerializer, StoreSerializer,EmployeeSerializer, RoomInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import StorePermission


class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = (StorePermission,)
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    # filter_fields = ('number', 'address')
    search_fields = ('number', 'address', 'chain__description')  # example POST: http://localhost:8000/stores/?search=ab0

"""
    def retrieve(self, request, pk=None):
        print ('!! has_object_permission')
        print ('@@ store retrieve: ' + pk)
"""

class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RoomInfoViewSet(viewsets.ModelViewSet):
    queryset = RoomInfo.objects.all()
    serializer_class = RoomInfoSerializer
