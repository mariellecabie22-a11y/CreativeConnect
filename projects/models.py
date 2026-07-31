from django.conf import settings
from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("closed", "Closed"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    deadline = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="open",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title