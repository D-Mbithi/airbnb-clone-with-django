from django.db import models

from core.models import TimeStampedModel


# Create your models here.
class List(TimeStampedModel):
    name = models.CharField(max_length=140)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of rooms"
    count_rooms.short_description = "Number of rooms"
