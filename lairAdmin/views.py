from django.shortcuts import render
from django.http import HttpResponse


def add_movies(request):
    return render(request, 'lairAdmin/addMovies.html')

# Create your views here.
