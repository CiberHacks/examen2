from django import forms
from core import models

class ToDoForm(forms.ModelForm):
    class Meta:
        model = models.ToDo
        fields = ['title', 'is_completed']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título del pendiente"}),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
