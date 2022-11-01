from django.contrib import admin
from django.utils.html import mark_safe
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


class PhotoInlineAdmin(admin.TabularInline):
    """
    Tabular Inline View for
    """

    model = Photo


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInlineAdmin,)

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "description",
                    "city",
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
        "total_rating",
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

    raw_id_fields = [
        "host",
    ]

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Amenity"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photos"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Defination"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width="50px" />')

    get_thumbnail.short_description = "Thumbnail"
