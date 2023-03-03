from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


def validate_unique_user(error_message, **criteria):
    existing_user = User.objects.filter(**criteria)

    if existing_user:
        raise forms.ValidationError(error_message)


class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Username', 'name': 'username'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(
        {'class': 'form-control', 'placeholder': 'Password', 'name': 'password'}))


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Username', 'name': 'username'}))
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'First name', 'name': 'first_name'}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(
        {'class': 'form-control', 'placeholder': 'Last name', 'name': 'last_name'}))
    email = forms.EmailField(label='Email', max_length=30, widget=forms.EmailInput(
        {'class': 'form-control', 'placeholder': 'Email', 'name': 'email'}))
    password = forms.CharField(label='Password', min_length=6, max_length=30, widget=forms.PasswordInput(
        {'class': 'form-control', 'placeholder': 'Password', 'name': 'password'}))
    confirm_password = forms.CharField(label='Confirm Password', min_length=6, max_length=30,
                                       widget=forms.PasswordInput(
                                           {'class': 'form-control', 'placeholder': 'Confirm password',
                                            'name': 'confirm_password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        validate_unique_user('Username already exists', username=username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        validate_unique_user('Email already exists', email=email)
        return email

    def clean_repeat_password(self):
        password = self.cleaned_data['password']
        repeat_password = self.cleaned_data['confirm_password']

        if password != repeat_password:
            raise forms.ValidationError('Passwords do not match')

        return repeat_password
