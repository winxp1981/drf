from rest_framework import viewsets
from retail.models import Chain, Store, Employee, RoomInfo
from retail.serializers import ChainSerializer, StoreSerializer,EmployeeSerializer, RoomInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.shortcuts import render

class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    # filter_fields = ('number', 'address')
    search_fields = ('number', 'address', 'chain__description')  # example POST: http://localhost:8000/stores/?search=ab0

class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RoomInfoViewSet(viewsets.ModelViewSet):
    queryset = RoomInfo.objects.all()
    serializer_class = RoomInfoSerializer


def retail_view (request):
    return render(request, 'index.html', {
        'data': "Hello Retail",
    })
