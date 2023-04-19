from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movies


class IndexView(generic.ListView):
    """Представление списка всех фильмов что есть в базе"""
    template_name = 'movies/index.html'
    context_object_name = 'movies_list'

    def get_queryset(self):
        """Возвращает все опубликованные фильмы на сайте"""
        all_movies = Movies.objects.all()
        return all_movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counter'] = [x for x in range(250)]
        return context


def detail(request, movie_slug):
    movie = get_object_or_404(Movies, slug=movie_slug)
    return render(request, 'movies/detail.html', {'movie': movie})


#Тест view
def test(request):
    return HttpResponse('Test')
