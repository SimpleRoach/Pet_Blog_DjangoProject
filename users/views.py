from django.shortcuts import render, redirect
from .forms import MySingupUsersForm, MyLoginUsersForm, ProfileFotoForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required


def user_login(request):

    if request.method == 'POST':
        form = MyLoginUsersForm(request.POST)
        data = {
            'title': 'Страница входа',
            'form': form
        }

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate (request, username = username,
                                 password = password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Вы успешно зашли!')
                return redirect('home')

            else:
                messages.error(request, 'Неверное имя пользователя или пароль')

        else:
            messages.error(request, 'Форма невалидна')

        return render(request,
                      'users/authorization.html',
                      data
                      )

    else:
        form = MyLoginUsersForm()
        data = {
            'title': 'Страница входа',
            'form': form
        }

        return render(request,
                      'users/authorization.html',
                      data
                      )


def user_logout(request):
    logout(request)
    messages.success(request,'Вы успешно вышли!')
    return redirect('home')


def user_signup(request):

    if request.method == 'POST':
        form = MySingupUsersForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')

    else:
        form = MySingupUsersForm()

    data ={
        'title': 'Страница регистрации',
        'form': form
    }
    return render(request,
                  'users/registration.html',
                  data
                  )


@login_required
def user_profile(request):
    profileForm = ProfileFotoForm()
    updateUserForm = ProfileUpdateForm()

    data = {
        'profileForm' : profileForm,
        'updateUserForm' : updateUserForm
    }
    return render(request,
                  'users/profile.html',
                  data
                  )