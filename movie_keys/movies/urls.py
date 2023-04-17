from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('detail/<slug:movie_slug>/', views.detail, name='detail'),

]