from django.shortcuts import render, redirect
from .forms import MyRegUsersForm, MySingUsersForm
from django.contrib import messages
from django.contrib.auth import login


def login(request):
    if request.method == 'POST':
        form = MySingUsersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зашли!')
            return redirect('home')
    form = MySingUsersForm()
    return render(request,
                  'users/authorization.html',
                  {
                      'title': 'Страница входа',
                      'form': form
                  })




def signup(request):
    if request.method == 'POST':
        form = MyRegUsersForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users/registration.html')
    else:
        form = MyRegUsersForm()

    form = MyRegUsersForm()

    return render(request,
                  'users/registration.html',
                  {
                      'title': 'Страница регистрации',
                      'form': form
                  })