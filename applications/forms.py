from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["cover_letter"]

        widgets = {
            "cover_letter": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": (
                        "Explain why you would be a good fit "
                        "for this project."
                    ),
                }
            ),
        }

        labels = {
            "cover_letter": "Application message",
        }