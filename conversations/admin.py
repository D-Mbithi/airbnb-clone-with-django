from django.contrib import admin
from .models import Message, Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
