from django import forms

from accounts.models import User

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "receiver",
            "subject",
            "content",
        ]

        widgets = {
            "receiver": forms.Select(
                attrs={"class": "form-select"}
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Message subject",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Write your message...",
                }
            ),
        }

    def __init__(self, *args, sender=None, **kwargs):
        super().__init__(*args, **kwargs)

        if sender is not None:
            self.fields["receiver"].queryset = (
                User.objects
                .exclude(pk=sender.pk)
                .order_by("username")
            )