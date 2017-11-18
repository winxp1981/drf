from rest_framework import viewsets
from .models import Room
from .models import RoomImage
from .serializers import ListRoomSerializer
from .serializers import RetrieveRoomSerializer
from .serializers import CreateRoomSerializer
from .serializers import RoomImageSerializer
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import RoomPermission
from .object import Task
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from django.db.models import Q
from functools import reduce
import operator


class RoomViewSet(viewsets.ModelViewSet):
#    queryset = Room.objects.all()    # 這裡拿掉queryset (override)的話, urls.py 要給 base_name
    serializer_class = ListRoomSerializer
    permission_classes = (RoomPermission,)
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    # filter_fields = ('number', 'address')
    search_fields = ('location', 'description')  # example POST: http://localhost:8000/stores/?search=ab0

    def get_serializer_class(self):
        print ('@@ view %s' % self.action)
        if self.action == 'list':
            return ListRoomSerializer
        if self.action == 'retrieve':
            print(self.request.user)
            return RetrieveRoomSerializer
        if self.action == 'create':
            #print ('@@ create room')
            return CreateRoomSerializer
        return self.serializer_class

    def get_queryset(self):
        print ('get_queryset@ RoomViewSet')
        queryset= Room.objects.all()
        q_list = []
        location = self.request.query_params.get('location', None)
        roomtype = self.request.query_params.get('roomtype', None)
        price = self.request.query_params.get('price', None)
        area = self.request.query_params.get('area', None)

        if location is not None:
            print ('location=%s' % location)
            q_list.append(Q(location__contains=location))

        if roomtype is not None:
            print ('roomtype=%s' % roomtype)
            q_list.append(Q(room_type__contains=roomtype))

        if price is not None:
            print ('price=%s' % price)
            if price == '_1W':
                print ('< 10000')
                q_list.append(Q(price_month__lt=10000))
            elif price == '1W_2W':
                print ('10000 <= x <= 20000')
                q_list.append(Q(price_month__gte=10000))
                q_list.append(Q(price_month__lte=20000))
            elif price == '2W_3W':
                print ('20000 <= x <= 30000')
                q_list.append(Q(price_month__gte=20000))
                q_list.append(Q(price_month__lte=30000))
            elif price == '3W_4W':
                print ('30000 <= x <= 40000')
                q_list.append(Q(price_month__gte=30000))
                q_list.append(Q(price_month__lte=40000))
            elif price == '4W':
                print ('40000 <= x <= 50000')
                q_list.append(Q(price_month__gte=40000))

        if area is not None:
            print ('area=%s' % area)
            if area == '_10P':
                print ('< 10p')
                q_list.append(Q(area__lt=10))
            elif area == '10P_20P':
                print ('10p <= x <= 20p')
                q_list.append(Q(area__gte=10))
                q_list.append(Q(area__lte=20))
            elif area == '20P_30P':
                print ('20p <= x <= 30p')
                q_list.append(Q(area__gte=20))
                q_list.append(Q(area__lte=30))
            elif area == '30P_40P':
                print ('30p <= x <= 40p')
                q_list.append(Q(area__gte=30))
                q_list.append(Q(area__lte=40))
            elif area == '40P_50P':
                print ('40p <= x <= 50p')
                q_list.append(Q(area__gte=40))
                q_list.append(Q(area__lte=50))
            elif area == '50P':
                print ('50p <= x')
                q_list.append(Q(area__gte=50))

        print ('get_queryset@RoomViewSet with %d conditions' % len(q_list))
        if len(q_list) > 0:
            return queryset.filter(reduce(operator.and_, q_list))
        else:
            return queryset
        # return Room.objects.all()

    @detail_route(methods=['post'])  # e.g. POST  http://localhost:8000/rooms/16/like/
    def like(self, request, pk=None):
        print ("%s like room %s" % (request.user, pk) )
        room = Room.objects.get(id=pk)
        room.who_likes.add(request.user)
    #    print (Room.objects.get(id=pk).who_likes.count())
        return Response(status=status.HTTP_200_OK)
        #return Response(status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])  # e.g. POST  http://localhost:8000/rooms/16/dislike/
    def dislike(self, request, pk=None):
        print ("%s like room %s" % (request.user, pk) )
        room = Room.objects.get(id=pk)
        room.who_likes.remove(request.user)
    #    print (Room.objects.get(id=pk).who_likes.count())
        return Response(status=status.HTTP_200_OK)
        #return Response(status=status.HTTP_400_BAD_REQUEST)
'''
    def destroy(self, request, pk=None):
        print ('delete room %s' % pk)
        return Response(status=status.HTTP_200_OK)
'''

"""
    def retrieve(self, request, pk=None):
        print ('!! has_object_permission')
        print ('@@ store retrieve: ' + pk)
"""


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer


"""
  Test non model ViewSet
"""
# Global variable used for the sake of simplicity.
# In real life, you'll be using your own interface to a data store
# of some sort, being caching, NoSQL, LDAP, external API or anything else
tasks = {
    1: Task(id=1, name='Demo', owner='xordoquy', status='Done'),
    2: Task(id=2, name='Model less demo', owner='xordoquy', status='Ongoing'),
    3: Task(id=3, name='Sleep more', owner='xordoquy', status='New'),
}


def get_next_task_id():
    return max(tasks) + 1


class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = TaskSerializer

    def list(self, request):
        print ('TaskViewSet::list request.method='+request.method)
        #  request.user returns an instance of django.contrib.auth.models.User
        print ('TaskViewSet::list request.user=', request.user)
        serializer = TaskSerializer(
            instance=tasks.values(), many=True)
        return Response(serializer.data)

    def create(self, request):
        print ('TaskViewSet::create request.method='+request.method)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.id = get_next_task_id()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(instance=task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(
            data=request.data, instance=task)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializer(
            data=request.data,
            instance=task,
            partial=True)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        del tasks[task.id]
        return Response(status=status.HTTP_204_NO_CONTENT)
