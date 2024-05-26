from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.forms import FileInput
from django.contrib import messages


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PhotoUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=FileInput)
    class Meta:
        model = Profile
        fields = ['image']




