from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Название статьи', max_length=100)
    text = models.TextField(verbose_name='Основной текст статьи')
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
