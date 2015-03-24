from django import forms
from app.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "home_phone", "mobile_phone", "email",)

        error_messages = {
            "first_name": {
                "required": "The first name is required",
            },
        }
