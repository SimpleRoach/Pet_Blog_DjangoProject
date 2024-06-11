from django.shortcuts import render
from .models import News


def home(request):
    data = {
        'news': News.objects.all().order_by('-id'),
        'title': 'Главная страница',
    }
    return render(
        request,
        'blog/home.html',
        data
    )





def contact(request):
    data = {
        'title': 'Страница контактов',
    }
    return render(
        request,
        'blog/contacti.html',
        data
    )

