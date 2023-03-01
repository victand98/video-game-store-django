from django.contrib.auth.forms import AuthenticationForm
from django import forms


class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'User name', 'name': 'username'}))
    password = forms.CharField(label='Password', max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password', 'name': 'password'}))
