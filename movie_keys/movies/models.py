import os
from django.conf import settings
from django.db import models


def poster_path():
    """Путь к постерам фильмов"""
    return os.path.join(settings.LOCAL_FILE_DIR, 'images/posters/')


class Movies(models.Model):
    """Модель для каталога фильмов"""
    name = models.CharField(max_length=100, blank=True)
    poster = models.ImageField(upload_to='poster')
    about = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name
