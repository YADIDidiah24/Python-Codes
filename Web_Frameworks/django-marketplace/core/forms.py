from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your username',
        'class': 'form-field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your password',
        'class': 'form-field'
    })) 

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your username',
        'class': 'form-field'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Your Email',
        'class': 'form-field'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your password',
        'class': 'form-field'
    }))   
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Reenter Your Password',
        'class': 'form-field'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
