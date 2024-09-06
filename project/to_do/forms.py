from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    model = User
    fields = ['email', 'password']


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time']