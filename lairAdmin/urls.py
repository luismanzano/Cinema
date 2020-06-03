from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'lairAdmin'

urlpatterns = [
    path('addMovies/', views.add_movies, name='addMovies'),
]
