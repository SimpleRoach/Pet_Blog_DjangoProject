from django.shortcuts import render, redirect
from .forms import MySingupUsersForm, MyLoginUsersForm
from django.contrib import messages
from django.contrib.auth import login


def login(request):
    if request.method == 'POST':
        form = MyLoginUsersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зашли!')
            return redirect('home')
    form = MyLoginUsersForm()
    return render(request,
                  'users/authorization.html',
                  {
                      'title': 'Страница входа',
                      'form': form
                  })




def signup(request):
    if request.method == 'POST':
        form = MySingupUsersForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users/registration.html')
    else:
        form = MySingupUsersForm()

    form = MySingupUsersForm()

    return render(request,
                  'users/registration.html',
                  {
                      'title': 'Страница регистрации',
                      'form': form
                  })