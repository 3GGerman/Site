import os
from django.conf import settings
from django.db import models
from django.urls import reverse


class Movies(models.Model):
    """Модель для каталога фильмов"""
    name = models.CharField(max_length=100, blank=True)
    poster = models.ImageField(upload_to='poster')
    about = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_slug': self.slug})
