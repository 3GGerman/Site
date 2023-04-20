from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movies


"""class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'movies_list'

    def get_queryset(self):
        
        all_movies = Movies.objects.all()
        return all_movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = [x for x in range(250)]
        return context"""


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
