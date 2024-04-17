from django.shortcuts import render
from .models import News


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Global page',
    }
    return render(request, 'blog/home.html', data)


# from django.http import HttpResponse


def contact(request):
    return render(request, 'blog/contacti.html', {'title': 'Страница контактов: '})
# Create your views here.
