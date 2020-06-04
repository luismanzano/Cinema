from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Movie
from . import forms

def add_movies(request):

        if request.method == 'POST':
            form = forms.AddMovie(request.POST)
            if form.is_valid():
                #save article to database
                instance = form.save(commit=False)
                instance.save()

        else: form = forms.AddMovie()
        return render(request, 'lairAdmin/addMovies.html', {'form': form})

def list_movies(request):

    movies = Movie.objects.all()
    return render(request, 'lairAdmin/listMovies.html', {'movies':movies})

def delete_movies(request, id):
    movie = Movie.objects.get(id = id)
    movie.delete()
    return redirect('lairAdmin:listMovies')

def edit_movies(request, id):
    movie = Movie.objects.get(id = id)
    return render(request, 'lairAdmin/listMovies.html', {'movie':movie})

# Create your views here.
