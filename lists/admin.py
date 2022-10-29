from django.contrib import admin
from .models import List


# Register your models here.
@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "count_rooms"]

    filter_horizontal = ["rooms"]

    search_fields = [
        "name",
    ]
