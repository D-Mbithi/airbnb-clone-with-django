from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

from core.models import TimeStampedModel
from users.models import CustomUser


class AbstractItem(TimeStampedModel):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """Type of Rooms."""

    class Meta:
        verbose_name = "Room Type"
        ordering = ("name",)


class Amenity(AbstractItem):
    """Amenity model defination."""

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facilty model defination."""

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """House Rules Model"""

    class Meta:
        verbose_name = "House Rule"


class Photo(TimeStampedModel):
    """Photo model defination."""

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        "Room",
        related_name="photos",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.caption


class Room(TimeStampedModel):
    """Room model."""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    bath = models.IntegerField()
    guest = models.IntegerField()
    checkin = models.TimeField()
    checkout = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        CustomUser,
        related_name="room",
        on_delete=models.CASCADE,
    )
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.SET_NULL,
        related_name="room",
        null=True,
        blank=True,
    )
    amenities = models.ManyToManyField(
        Amenity,
        related_name="room",
        blank=True,
    )
    facilities = models.ManyToManyField(
        Facility,
        related_name="room",
        blank=True,
    )
    house_rules = models.ManyToManyField(
        HouseRule,
        related_name="room",
        blank=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = self.city.capitalize()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        if len(all_reviews) > 0:
            all_ratings = [review.rating_avg() for review in all_reviews]

            return round(sum(all_ratings) / len(all_ratings), 2)
        return 0
