# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=255, widget=forms.EmailInput(attrs={'autofocus': True}))
