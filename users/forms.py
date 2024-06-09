from django import forms
from django.contrib.auth.models import User

from .models import Profile


class MyLoginUsersForm(forms.Form):
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


class MySingupUsersForm(forms.Form):
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
    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=data['password1']
        )
        return user


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже занято")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Пароли не совпадают")

        return cleaned_data
    class Meta:
        model = User
        fields = ['email',
                  'username',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'
                  ]

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             max_length=254,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control'}))
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username',
                                   'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['email',
                  'username',
                  ]
class ProfileFotoForm(forms.Form):
    image = forms.ImageField(required=False,
                             label='Загрузить фото',
                             )

    class Meta:
        model = Profile
        fields = ['image']
