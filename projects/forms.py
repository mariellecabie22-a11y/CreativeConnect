from django import forms
from django.core.exceptions import ValidationError

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = [
            "title",
            "description",
            "category",
            "location",
            "deadline",
            "status",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Project title",
                    "required": True,
                    "maxlength": 200,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Describe the project and who you need.",
                    "required": True,
                    "maxlength": 3000,
                    "data-character-counter": "description-counter",
                }
            ),
            "category": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Short film",
                    "required": True,
                    "maxlength": 100,
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Dublin",
                    "required": True,
                    "maxlength": 100,
                }
            ),
            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "required": True,
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if not title:
            raise ValidationError(
                "Please enter a project title."
            )

        return title

    def clean_description(self):
        description = self.cleaned_data["description"].strip()

        if len(description) < 20:
            raise ValidationError(
                "Please provide at least 20 characters describing your project."
            )

        return description

    def clean_category(self):
        category = self.cleaned_data["category"].strip()

        if not category:
            raise ValidationError(
                "Please enter a project category."
            )

        return category

    def clean_location(self):
        location = self.cleaned_data["location"].strip()

        if not location:
            raise ValidationError(
                "Please enter a location."
            )

        return location