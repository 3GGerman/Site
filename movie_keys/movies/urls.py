from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('detail/<slug:movie_slug>/', views.detail, name='detail'),
    path('test/', views.test, name='test'),

]