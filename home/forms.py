from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={"type": "text", "class": "form-control"})
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )



