from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import WorkoutsByDays


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Login",
        widget=forms.TextInput(
            attrs={"class": "login-input", "placeholder": "Enter Login"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "password-input", "placeholder": "Enter Password"}
        ),
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Login",
        widget=forms.TextInput(
            attrs={"class": "login-input", "placeholder": "Enter Login"}
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "email-input", "placeholder": "Enter Email"}
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "password1-input", "placeholder": "Enter Password"}
        ),
    )
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(
            attrs={"class": "password2-input", "placeholder": "Repeat Password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class WorkoutsByDaysForm(forms.ModelForm):
    class Meta:
        model = WorkoutsByDays
        fields = [
            "day",
            "category_name",
            "workouts",
            "time_coefficient",
            "is_completed",
        ]
        widgets = {
            "is_completed": forms.CheckboxInput(
                attrs={"class": "is_completed-checkbox", "checked": True}
            )
        }
