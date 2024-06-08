from django.shortcuts import render, redirect
from .forms import MySingupUsersForm, MyLoginUsersForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login


def user_login(request):
    if request.method == 'POST':
        form = MyLoginUsersForm(request.POST)
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
                      {
                          'title' : 'Страница входа',
                          'form' : form
                      })
    else:
        form = MyLoginUsersForm()
        return render(request,
                      'users/authorization.html',
                      {
                          'title': 'Страница входа',
                          'form': form
                      })
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

    return render(request,
                  'users/registration.html',
                  {
                      'title': 'Страница регистрации',
                      'form': form
                  })
