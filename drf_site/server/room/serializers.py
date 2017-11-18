from rest_framework import serializers
from .models import Room
from .models import RoomImage
from .object import Task

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ("room", "photo", )
        # TODO: GET/POST 分開!!!
'''
    def create(self, validated_data):
        print ('RoomImageSerializer::create %d', validated_data.get('room'))
        return RoomImage.objects.create(**validated_data)
'''



# GET /rooms
class ListRoomSerializer(serializers.ModelSerializer):
    # room_photos = RoomImageSerializer(many=True)
    room_thumb = serializers.SerializerMethodField()

    # see http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    # 對應 get_like_count, 取出 many to many user count
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ("id", "title", "description", "price_month", "room_thumb", "like_count", "location", "room_type", "area", "layout", "floor")
        # fields = ("id", "title", "description", "price_month", "room_photos", "like_count")
        # fields = '__all__'

    def get_like_count(self, obj):
        return obj.who_likes.count()

    # 只回傳第一張當做 thumbnail image
    def get_room_thumb(self, obj):
        query = obj.room_photos.first()
        request = self.context.get('request')
        serializer = RoomImageSerializer(query, many=False, context={'request': request})      # 註: 傳 request context 進去才能 build 出 full url
        return serializer.data


# GET /rooms/id
class RetrieveRoomSerializer(serializers.ModelSerializer):
    room_photos = RoomImageSerializer(many=True)

    # 現在登入的user是否收藏
    is_user_like = serializers.SerializerMethodField()

    class Meta:
        model = Room
    #    fields = ('id', 'room_photos')
        fields = '__all__'

    def get_is_user_like(self, obj):
        print ('user id: ', self.context['request'].user.id);
        # print (obj)
        return (obj.who_likes.filter(id=self.context['request'].user.id).count())

# POST /rooms
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
    #    fields = ('id', 'room_photos')
        fields = '__all__'

"""
  Test non model TaskSerializer
"""
STATUSES = (
    'New',
    'Ongoing',
    'Done',
)


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)
    status = serializers.ChoiceField(choices=STATUSES, default='New')

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
