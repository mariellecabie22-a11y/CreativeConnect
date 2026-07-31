from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email", "").lower().strip()

        if not email:
            raise ValidationError(
                "Please enter an email address."
            )

        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(
                "An account with this email already exists."
            )

        return email