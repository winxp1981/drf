from rest_framework import serializers
from .models import Room
from .models import RoomImage

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ("room", "photo", )
'''
    def create(self, validated_data):
        print ('RoomImageSerializer::create %d', validated_data.get('room'))
        return RoomImage.objects.create(**validated_data)
'''

class RoomSerializer(serializers.ModelSerializer):
    room_photos = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "title", "description", "price_month", "room_photos")
        # fields = ("url", "title", "description", "price_month", "room_photos")
        # fields = '__all__'
