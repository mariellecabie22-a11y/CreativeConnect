from django.contrib import admin

from .models import CreativeProfile


@admin.register(CreativeProfile)
class CreativeProfileAdmin(admin.ModelAdmin):
    list_display = [
        "display_name",
        "creative_type",
        "location",
        "available_for_projects",
    ]

    list_filter = [
        "creative_type",
        "experience_level",
        "available_for_projects",
    ]

    search_fields = [
        "display_name",
        "location",
        "bio",
    ]