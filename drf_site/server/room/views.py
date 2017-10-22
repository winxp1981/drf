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


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
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
