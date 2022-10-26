from django.contrib import admin
from .models import Room, RoomType, HouseRule, Amenity, Facility, Photo


# Register your models here.
@admin.register(RoomType, HouseRule, Amenity, Facility)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "used_by",
    ]

    def used_by(self, obj):
        return obj.room.count()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                )
            },
        ),
        ("Times", {"fields": ("checkin", "checkout", "instant_book")}),
        ("Spaces", {"fields": ("guest", "bedrooms", "beds", "bath")}),
        (
            "More about spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last details", {"fields": ("host",)}),
    )

    list_display = [
        "name",
        "country",
        "city",
        "price",
        "bedrooms",
        "beds",
        "bath",
        "checkin",
        "checkout",
        "instant_book",
        "room_type",
        "count_amenities",
        "count_photos",
    ]
    search_fields = ["=city", "host__usernames"]
    list_filter = [
        "host__super_host",
        "instant_book",
        "room_type",
        "bedrooms",
        "room_type",
        "country",
        "amenities",
        "city",
        "house_rules",
    ]
    filter_horizontal = [
        "amenities",
        "facilities",
        "house_rules",
    ]

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Amenity"

    def count_photos(self, obj):
        return object.photos.count()

    count_photos.short_description = "Photos"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
