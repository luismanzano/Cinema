from django import forms

from lairAdmin import models

class AddMovie(forms.ModelForm):
    class Meta:
       model = models.Movie 
       fields = ['title', 'duration', 'cast', 'director', 'genre', 'language', 'mode', 'showing'] 