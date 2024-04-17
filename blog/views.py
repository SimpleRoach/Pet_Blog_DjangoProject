from django.shortcuts import render


def home(request):
    number = 1

    news = [
        {
            'title': 'Главная новость',
            'text': 'Самая первая версия сайта',
            'date': '16.04.24',
            'avtor': 'admin'
        },
        {
            'title': 'Дополнение',
            'text': 'Сейчас просто знакомлюсь с функционалом фреймворка Django',
            'date': '16.04.24',
            'avtor': 'admin'
        }
    ]
    data = {
        'news': news,
        'title': 'Global page',
    }
    return render(request, 'blog/home.html', data)


# from django.http import HttpResponse


def contact(request):
    return render(request, 'blog/contacti.html', {'title': 'Страница контактов: '})
# Create your views here.
