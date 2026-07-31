from django.conf import settings
from django.db import models


class CreativeProfile(models.Model):
    CREATIVE_TYPES = [
        ("actor", "Actor"),
        ("director", "Director"),
        ("musician", "Musician"),
        ("photographer", "Photographer"),
        ("writer", "Writer"),
        ("editor", "Editor"),
        ("designer", "Designer"),
        ("other", "Other"),
    ]

    EXPERIENCE_LEVELS = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("experienced", "Experienced"),
        ("professional", "Professional"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="creative_profile",
    )

    display_name = models.CharField(max_length=100)

    creative_type = models.CharField(
        max_length=30,
        choices=CREATIVE_TYPES,
    )

    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVELS,
    )

    bio = models.TextField(blank=True)
    location = models.CharField(max_length=120)

    portfolio_url = models.URLField(blank=True)

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    available_for_projects = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name