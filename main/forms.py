from django.forms import ModelForm, TextInput
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        exclude = ("user",)
        widgets = {
            'deadline':TextInput(attrs={'type':'datetime-local'}),
        }