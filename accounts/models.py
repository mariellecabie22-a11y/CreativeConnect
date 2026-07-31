from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model for CreativeConnect."""

    def __str__(self):
        return self.usernames