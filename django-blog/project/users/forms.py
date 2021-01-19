from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # This is where you would add additional fields to a form
    email = forms.EmailField()

    class Meta:
        # This is where you choose the model this will impact and what new fields will be displayed
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']