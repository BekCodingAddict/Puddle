from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("username", "email", "password1", "password2")


    username=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Your username",
        "class":'w-full py-4 px-6 rounded-xl bg-stone-50'
    }))

    email=forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder":"Your email",
        "class":'w-full py-4 px-6 rounded-xl bg-stone-50'
    }))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Your password",
        "class":'w-full py-4 px-6 rounded-xl bg-stone-50'
    }))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm password",
        "class":'w-full py-4 px-6 rounded-xl bg-stone-50'
    }))