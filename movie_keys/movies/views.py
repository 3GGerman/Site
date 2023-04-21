from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movies



def index(request):
    all_movies = Movies.objects.all()
    context = {
        'all_movies': all_movies,
        'counter': [x for x in range(250)],
    }
    return render(request, 'movies/index.html', context=context)


def detail(request, movie_slug):
    movie = get_object_or_404(Movies, slug=movie_slug)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context=context)


#Тест view
def test(request):
    return HttpResponse('Test')
