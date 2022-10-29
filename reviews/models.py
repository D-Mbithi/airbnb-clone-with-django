from django.db import models
from core.models import TimeStampedModel


class Review(TimeStampedModel):
    """Review Model Defination."""

    review = models.TextField()
    accuracy = models.IntegerField()
    cleanliness = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    checkin = models.IntegerField()
    value = models.IntegerField()
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "users.User", related_name="host", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_avg(self):
        avg = (
            sum(
                [
                    self.cleanliness,
                    self.communication,
                    self.location,
                    self.checkin,
                    self.value,
                    self.accuracy,
                ]
            )
            / 6
        )

        return round(avg, 2)
