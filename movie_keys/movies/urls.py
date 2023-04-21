from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<slug:movie_slug>/', views.detail, name='detail'),
    path('test/', views.test, name='test'),

]