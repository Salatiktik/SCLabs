from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput({'class': 'input','type':'password'}))
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True, min_length=3)
    password = forms.CharField(widget=forms.PasswordInput())
    passwordConfirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cd = self.cleaned_data
        password1 = cd.get("password")
        password2 = cd.get("passwordConfirm")
        if password1 != password2:
            raise forms.ValidationError("Passwords did not match")

        return cd

