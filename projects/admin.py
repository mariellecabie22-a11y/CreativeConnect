from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "category",
        "location",
        "status",
        "deadline",
    )

    list_filter = (
        "status",
        "category",
    )

    search_fields = (
        "title",
        "description",
    )