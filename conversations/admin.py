from django.contrib import admin
from .models import Message, Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Message Admin Defination."""

    list_display = ["__str__", "count_messages", "count_participants"]

    filter_horizontal = ["participants"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Message Admin Definition."""

    list_display = ["__str__", "created"]
