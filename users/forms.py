from django import forms
from django.contrib.auth.models import User


# from django.contrib.auth.forms import UserCreationForm
class MySingUsersForm(forms.Form):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control'}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Пароль',
                                    'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password1'
        ]


# MyRegUsersForm
class MyRegUsersForm(forms.Form):
    email = forms.EmailField(required=True,
                             max_length=254,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control'}))
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control'}))
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Имя',
                                     'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Фамилия',
                                    'class': 'form-control'}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Пароль',
                                    'class': 'form-control'}))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Подтвердите пароль',
                                    'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email',
                  'username',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'
                  ]
