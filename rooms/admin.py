from django.contrib import admin
from .models import Room, RoomType, HouseRule, Amenity, Facility, Photo


# Register your models here.
@admin.register(RoomType, HouseRule, Amenity, Facility)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
