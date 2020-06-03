from django.db import models

# Create your models here.
class Movie(models.Model):
    title   = models.CharField(max_length=200)
    duration = models.DurationField()
    cast  = models.TextField()
    director = models.CharField(max_length=200)
    genre   = models.CharField(max_length=200)
    language   = models.CharField(max_length=200)
    #thumb   = models.ImageField(upload_to = os.path.join(BASE_DIR))
    mode = models.IntegerField(default = 0)
    showing = models.BooleanField(default = False)
    #anadir los archivos estaticos para la thumb