from django import forms
from django.forms import ModelForm
from .models import Member


class RegisterForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ["name", "email", "password", "prefers"]
