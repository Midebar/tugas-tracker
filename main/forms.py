from django.forms import ModelForm, TextInput
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "amount",
            "description",
            "deadline",
        ]

        widgets = {
            'deadline':TextInput(attrs={'type':'datetime-local'}),
        }