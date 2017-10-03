from django.contrib import admin
from .models import Room
from .models import RoomImage

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'title', 'description', 'location', 'area', 'layout', 'parking', 'price_month', 'deposit')

class RoomImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'photo')

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage, RoomImageAdmin)

'''
title         [標題]
description   [說明]
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
