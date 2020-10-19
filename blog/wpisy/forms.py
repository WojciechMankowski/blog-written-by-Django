from django import forms
from .models import kontakt


class Kontakt(forms.ModelForm):
    class Meta:
        model = kontakt
        fields = ("Name", "Email", "Title", "Message")
        labels = {
            "Name": "Twoje imię",
            "Email": "E-mail",
            "Title": "Tytuł wiadomości",
            "Message": "Wiadomość",
        }
