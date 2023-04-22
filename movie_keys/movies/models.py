import os
from django.conf import settings
from django.db import models
from django.urls import reverse


class Movies(models.Model):
    """Модель для каталога фильмов"""
    title = models.CharField(max_length=100, blank=True, verbose_name='Название фильма')
    poster = models.ImageField(upload_to='poster', verbose_name='Постер')
    release_dates = models.IntegerField(verbose_name='Год')
    about = models.TextField(blank=True, verbose_name='О фильме')
    date_create = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_slug': self.slug})

    #Класс для админ-панельки
    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'
        ordering = ['date_create', 'id', 'title']