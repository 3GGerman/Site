import os
from django.conf import settings
from django.db import models


def poster_path():
    """Путь к постерам фильмов"""
    return os.path.join(settings.LOCAL_FILE_DIR, 'images/posters/')


class Movies(models.Model):
    """Модель для каталога фильмов"""
    movie_name = models.CharField(max_length=100)
    #movie_poster = models.FilePathField(path=poster_path)
    movie_about = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.movie_name