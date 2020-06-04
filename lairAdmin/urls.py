from django.contrib import admin
from django.urls import path, include
from lairAdmin import views

app_name = 'lairAdmin'

urlpatterns = [
    path('addMovies/', views.add_movies, name='addMovies'),
    path('listMovies/', views.list_movies, name='listMovies'),
    path('deleteMovies/<id>', views.delete_movies, name='deleteMovies'),
    path('editMovies/<id>', views.edit_movies, name='editMovies'),
    #path('updateMovies/<id>', views.update_movies, name='updateMovies'),
    

]
