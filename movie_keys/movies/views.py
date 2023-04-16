from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Movies

counter = [1, 2, 3]


class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'movies_list'

    def get_queryset(self):
        """Возвращает все опубликованные фильмы на сайте"""
        more_movie = Movies.objects.all()
        for i in range(3):
            more_movie = more_movie.union(more_movie, all=True)
        return more_movie



