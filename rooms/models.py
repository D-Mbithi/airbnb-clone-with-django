from django.db import models
from django_countries.fields import CountryField
from users.models import User
from core.models import TimeStampedModel


class AbstractItem(TimeStampedModel):

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class RoomType(AbstractItem):
    """ Type of Rooms. """

    class Meta:
        verbose_name = 'Room Type'
        ordering = ('name',)


class Amenity(AbstractItem):

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = 'Amenities'


class Facility(AbstractItem):

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem):
    """House Rules Model"""

    class Meta:
        verbose_name = 'House Rule'


class Photo(TimeStampedModel):
    caption = models.CharField(max_length=100)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(TimeStampedModel):
    """ Room model. """

    name            = models.CharField(max_length=140)
    description     = models.TextField()
    country         = CountryField()
    city            = models.CharField(max_length=80)
    price           = models.IntegerField()
    address         = models.CharField(max_length=140)
    bedrooms        = models.IntegerField()
    beds            = models.IntegerField()
    bath            = models.IntegerField()
    guest           = models.IntegerField()
    checkin         = models.TimeField()
    checkout        = models.TimeField()
    instant_book    = models.BooleanField(default=False)
    host            = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type       = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    amenities       = models.ManyToManyField(Amenity, blank=True)
    facilities      = models.ManyToManyField(Facility,  blank=True)
    houserules      = models.ManyToManyField(HouseRule,  blank=True)

    def __str__(self):
        return self.name
