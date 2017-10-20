from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

'''
location      [位置]     地址
area          [坪數]
layout        [格局]     4/2/2  (房/廳/衛)
floor         [樓層]     12/15
direction     [朝向]
age           [屋齡]
building_type [類型]     電梯大樓, 公寓, 透天, 別墅
room_type     [房型]     獨立套房, 分租套房, 雅房, 整層住家
parking       [有車位]    bool
price_month   [租金/月]
price_quarter [租金/季]
price_year    [租金/年]
deposit       [押金]     月
mgmt_fee      [管理費]
title         [標題]
description   [說明]
host          [屋主]     foreign key to a User

balcony       [有陽台]     bool
pet           [可養寵物]   bool
cook          [可開伙]     bool
mrt           [近捷運]     bool
tv            [有電視]     bool
ac            [有冷氣]     bool
ref           [有冰箱]     bool
water_hearter [有熱水器]   bool
natural_gas   [有天然瓦斯]  bool
cabel_tv      [有第四台]   bool
network       [有網路]     bool
wash_machine  [有洗衣機]   bool
bed           [床]        bool
wardrobe      [衣櫃]      bool
table         [桌子]      bool
sofa          [沙發]      bool
chair         [椅子]      bool

'''

class Room(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    host = models.ForeignKey(User, blank=True)
    location = models.CharField(max_length=100)
    area = models.IntegerField(blank=True)
    layout = models.CharField(max_length=20, blank=True)
    floor  = models.CharField(max_length=20)
    direction  = models.CharField(max_length=20, blank=True)
    who_likes = models.ManyToManyField(User, related_name='who_likes', blank=True)

    age = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    building_type  = models.CharField(max_length=20, blank=True)
    room_type  = models.CharField(max_length=20, blank=True)
    parking = models.BooleanField(blank=True)

    price_month = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    price_quarter = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    price_year = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    deposit = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    mgmt_fee = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    balcony = models.BooleanField(blank=True)
    pet  = models.BooleanField(blank=True)
    cook = models.BooleanField(blank=True)
    mrt = models.BooleanField(blank=True)
    tv = models.BooleanField(blank=True)
    ac = models.BooleanField(blank=True)
    ref = models.BooleanField(blank=True)
    water_hearter = models.BooleanField(blank=True)
    natural_gas = models.BooleanField(blank=True)
    cabel_tv = models.BooleanField(blank=True)
    network = models.BooleanField(blank=True)
    wash_machine = models.BooleanField(blank=True)
    bed = models.BooleanField(blank=True)
    wardrobe = models.BooleanField(blank=True)
    table = models.BooleanField(blank=True)
    sofa = models.BooleanField(blank=True)
    chair = models.BooleanField(blank=True)

    def __str__(self):
        return self.title


class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='room_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='rooms')

#    def __str__(self):
#        return self.photo.url
