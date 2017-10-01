from django.contrib import admin
from .models import Chain, Store, Employee, RoomInfo

class ChainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'slogan', 'founded_date', 'website')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','chain', 'number', 'address', 'opening_date')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','store', 'number', 'first_name', 'last_name', 'hired_date')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id','description', 'photo')


admin.site.register(Chain, ChainAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RoomInfo, RoomAdmin)