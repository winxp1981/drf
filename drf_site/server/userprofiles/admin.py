from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Profile._meta.fields]

admin.site.register(Profile, ProfileAdmin)
