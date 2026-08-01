from django import forms

from .models import CreativeProfile


class CreativeProfileForm(forms.ModelForm):
    class Meta:
        model = CreativeProfile

        fields = [
            "display_name",
            "creative_type",
            "experience_level",
            "bio",
            "location",
            "portfolio_url",
            "profile_image",
            "available_for_projects",
        ]

        widgets = {
            "display_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your public display name",
                }
            ),
            "creative_type": forms.Select(
                attrs={"class": "form-select"}
            ),
            "experience_level": forms.Select(
                attrs={"class": "form-select"}
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell people about your creative work.",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Dublin",
                }
            ),
            "portfolio_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://yourportfolio.com",
                }
            ),
            "profile_image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
            "available_for_projects": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }