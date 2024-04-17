from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import MyRegUsersForm, MySingUsersForm
from django.contrib import messages


def singup(request):
    if request.method == 'POST':
        form = MySingUsersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зашли!')
            return redirect('home')
    form = MySingUsersForm()
    return render(request,
                  'users/registration.html',
                  {
                      'title': 'Страница входа',
                      'form': form
                  })


def regis(request):
    if request.method == 'POST':
        form = MyRegUsersForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')

    else:
        form = MyRegUsersForm()

    form = MyRegUsersForm()
    return render(request,
                  'users/registration.html',
                  {
                      'title': 'Страница регистрации',
                      'form': form
                  })
# Create your views here.
