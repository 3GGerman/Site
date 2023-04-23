from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movies


def index(request):
    search = request.POST.get('search')
    if search:
        all_movies = Movies.objects.filter(title__istartswith=search)
        context = {
            'all_movies': all_movies,
            'counter': [x for x in range(250)],
        }
        return render(request, 'movies/index.html', context=context)
    else:
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


def about(request):
    return render(request, 'movies/about.html')


#Тест view
def test(request):
    return HttpResponse('Test')
