from rest_framework import serializers
from .models import Room
from .models import RoomImage

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
    room_photos = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "title", "description", "price_month", "room_photos")
        # fields = ("url", "title", "description", "price_month", "room_photos")
        # fields = '__all__'

# GET /rooms/id
class RetrieveRoomSerializer(serializers.ModelSerializer):
    room_photos = RoomImageSerializer(many=True)

    class Meta:
        model = Room
    #    fields = ('id', 'room_photos')
        fields = '__all__'

# POST /rooms
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
    #    fields = ('id', 'room_photos')
        fields = '__all__'
