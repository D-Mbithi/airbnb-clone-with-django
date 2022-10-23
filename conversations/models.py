from django.db import models
from core.models import TimeStampedModel


# Create your models here.
class Conversation(TimeStampedModel):
    """
    Conversation model Defination
    """

    paticipants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return self.created


class Message(TimeStampedModel):
    """
    Message model Defination
    """

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "conversations.Conversation", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} Says: {self.message}"
