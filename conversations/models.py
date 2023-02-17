from django.db import models

from core.models import TimeStampedModel


# Create your models here.
class Conversation(TimeStampedModel):
    """
    Conversation model Defination
    """

    participants = models.ManyToManyField("users.CustomUser", blank=True)

    def __str__(self):

        usernames = ", ".join([user.username for user in self.participants.all()])
        return str(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of messages"

    def count_participants(self):
        return self.participants.count()


class Message(TimeStampedModel):
    """
    Message model Defination
    """

    message = models.TextField()
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "conversations.Conversation",
        related_name="messages",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} Says: {self.message}"
        return f"{self.user} Says: {self.message}"
