from django.contrib import admin

# Register your models here.
from .models import Movies


class MoviesAdmin(admin.ModelAdmin):
    """Для отображения доп.инфо. списка фильмов"""
    list_display = ['id', 'title', 'poster', 'date_create', 'is_published']
    list_display_links = ['id', 'title']


admin.site.register(Movies, MoviesAdmin)